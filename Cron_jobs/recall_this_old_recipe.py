#!/data/data/com.termux/files/usr/bin/python3

import os
import sqlite3
import asyncio
import logging
from dotenv import load_dotenv
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import nest_asyncio
import sys

#link to my repo
dir = '/storage/emulated/0/MHDM_git'
custom_libs = os.path.join(dir, 'Custom_Libraries')
sys.path.append(custom_libs)

#my own modules
import SQL_utilities
import Utilities


# Define the path for the database file
db_directory = "database"
db_path = os.path.join(dir, db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

formatted_recipe = "Do you remember this old recipe? \n \n" + SQL_utilities.random_recipe(cursor)

### communication with telegram ###

#Load the .env file
result = load_dotenv(dotenv_path=f'{dir}/.env')

#Get the token from the environment variable
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

import os
import sqlite3
import asyncio
import logging
from dotenv import load_dotenv
from telegram import Bot
import sys

# Link to my repo
dir = '/storage/emulated/0/MHDM_git'
custom_libs = os.path.join(dir, 'Custom_Libraries')
sys.path.append(custom_libs)

# My own modules
import SQL_utilities

# Define the path for the database file
db_directory = "database"
db_path = os.path.join(dir, db_directory, "recipes.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

formatted_recipe = "Do you remember this old recipe? \n\n" + SQL_utilities.random_recipe(cursor)

### Communication with Telegram ###

# Load the .env file
load_dotenv(dotenv_path=f'{dir}/.env')

# Get the token and chat ID from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to send the initial message
async def send_initial_message():
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=formatted_recipe)
    logging.info(f"Message sent to chat ID {chat_id}")

# Main function
if __name__ == "__main__":
    asyncio.run(send_initial_message())
