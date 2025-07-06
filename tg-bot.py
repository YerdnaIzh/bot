import config
import asyncio
import telegram

async def main():
    bot = telegram.Bot(config.BOT_TOKEN)
    async with bot:
        await bot.send_message(text = 'Hi, John!', chat_id = 453654630)

if __name__ == '__main__':
    asyncio.run(main())
