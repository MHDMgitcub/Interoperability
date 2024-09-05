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
import utilities


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

# Apply nest-asyncio to the current event loop
nest_asyncio.apply()

# Create a function to handle incoming messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logging.info(f"Received message: {user_message}")
    await update.message.reply_text(f"Thank you for your response: {user_message}!'")

# Create a function to send the initial message
async def send_initial_message(bot: Bot):
    await bot.send_message(chat_id=chat_id, text=formatted_recipe)

# Main function to run the bot
async def main():
    application = ApplicationBuilder().token(bot_token).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    bot = Bot(token=bot_token)
    await send_initial_message(bot)

    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
