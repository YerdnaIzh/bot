from pyrogram.types import KeyboardButton
from pyrogram import emoji


back_button = KeyboardButton(f"{emoji.BACK_ARROW} Back")

time_button = KeyboardButton(f"{emoji.ALARM_CLOCK} Time")
help_button = KeyboardButton(f"{emoji.WHITE_QUESTION_MARK} Help")
settings_button = KeyboardButton(f"{emoji.GEAR} Settings")
random_films = KeyboardButton(f"Random Films")
search_films = KeyboardButton(f"Search Films")

# Домашнее задание/TODO:
# Создайте кнопки для /search_films и /random_films
