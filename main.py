import time
import random
import asyncio
import logging
import requests

import pyrogram
from pyrogram import Client, filters, emoji
from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup
from pyrogram.types import Message

import config
import operator

from database import Database

from kinopoisk import config_request, print_film

def get_random_cat():
	url = "https://catass.com/cat"
	response = requests.get(f"{url}?json=true")
	cat_id = response.json()["_id"]
	cat_url = f"{url}/{cat_id}"

	return cat_url

class Client(Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.database = Database()

	def stop(self, *args, **kwargs):
		self.database.close()
		return super().stop(*args, **kwargs)

api_id = config.API_ID
api_hash = config.API_HASH
bot_token = config.BOT_TOKEN

app = Client("my_account", api_id = api_id, api_hash = api_hash, bot_token = bot_token)

back_button = KeyboardButton(f"{emoji.BACK_ARROW} Back")
start_button = KeyboardButton(f"Start")

main_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [back_button],
            [start_button]
        ],
        resize_keyboard=True,
)

def button_filter(button: KeyboardButton):
    async def func(_, __, message: Message):
        return message.text == button.text

    return filters.create(func, "ButtonFilter", button=button)

@app.on_message(filters=filters.command("calc"))
async def calc_command(Client, message):
    ops = {
            "+": operator.add, "-": operator.sub,
            "*": operator.mul, "/": operator.truediv,
    }

    if len(message.command) != 4:
        return await message.reply("Wrong amount of arguments!")

    _, left, op, right = message.command
    op = ops.get(op)
    if op is None:
        return await message.reply("Unknown operator")
    if not left.isdigit() or not right.isdigit():
        return await message.reply("Arguments must be numbers")

    left, right = int(left), int(right)
    await message.reply(f"Result: {op(left, right)}")

@app.on_message(filters=filters.command("start") | button_filter(start_button))
async def test(client, message):
	user = client.database.get_user(message.from_user.id)
	print(user.__dict__ if user else None)
	if user is None:
		client.database.create_user(message.from_user.id)
	
	await message.reply("Hello, user!", reply_markup=main_keyboard)
	print("Hello, user!")

@app.on_message(filters=filters.command("time"))
async def test(client, message):
    current_time = time.strftime("%I:%M:%S")
    await message.reply(f"__Current time: {current_time}__")

@app.on_message(filters=filters.command("cat"))
async def test(client, message):
	cat = get_random_cat()
	await message.reply(cat)

@app.on_message(filters=filters.command("echo"))
async def echo(client, message):
    text = message.text
    if random.choice([True, False]):
        print(text)
        await message.reply(text)
    else:
        print(text[::-1])
        await message.reply(text[::-1])

@app.on_message(filters = filters.command("random_films"))
async def send_random_film(client: Client, message: Message):
	response = config_request("random")
	if 'error' in response:
		await message.reply(response['error'])
		return
	film_message = print_film(response)
	await message.reply(film_message, reply_markup = keyboards.film_inline_keyboard)

@app.on_message(filters = filters.command("find_film"))
async def find_film_by_name(client, message):
	query = message.text.split(maxsplit=1)
	if len(query) < 2:
		await message.reply("Please enter a film name after /find_film")
		return
	film_name = query[1]
	print(film_name)
	params = {"name": film_name}
	response = config_request("", params=params)
	
	print(response)
	film_message = print_film(response['docs'][0])
	await message.reply(film_message)

app.run()
