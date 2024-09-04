#!/data/data/com.termux/files/usr/bin/python3

import os
import asyncio
import datetime
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv



dir =  '/storage/emulated/0/MHDM_git'

# Load the .env file
result = load_dotenv(dotenv_path=f'{dir}/.env')

#print(f"dotenv loaded: {result}")

# Get the token from the environment variable
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# The reminder message
message = "Cron test You have a doctor's appointment at 1:30 PM today."

async def send_reminder():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

if __name__ == "__main__":
    asyncio.run(send_reminder()) 