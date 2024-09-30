#!/data/data/com.termux/files/usr/bin/python3

import os
import sqlite3
import asyncio
import logging
import json
from dotenv import load_dotenv
from telegram import Bot
import sys
from datetime import datetime

# Link to my repo
dir = '/storage/emulated/0/MHDM_git'
custom_libs = os.path.join(dir, 'Custom_Libraries')
sys.path.append(custom_libs)

# My own modules
import SQL_utilities

# Define the path for the database file and the log file
db_directory = "database"
db_path = os.path.join(dir, db_directory, "recipes.db")
log_file_path = os.path.join(dir, "task_log.json")

# Check if the script has already run today
def already_ran_today():
    if not os.path.exists(log_file_path):
        return False  # No log means it hasn't run yet
    
    with open(log_file_path, 'r') as file:
        logs = json.load(file)

    today = datetime.now().strftime("%Y-%m-%d")
    return any(entry['date'] == today for entry in logs)  # True if today’s date is in the log

# Update the log file with today's run status
def log_run(status, message):
    today = datetime.now().strftime("%Y-%m-%d")
    execution_time = datetime.now().strftime("%H:%M:%S")
    log_entry = {
        "date": today,
        "status": status,
        "message": message,
        "execution_time": execution_time
    }
    
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r+') as file:
            logs = json.load(file)
            logs.append(log_entry)
            file.seek(0)
            json.dump(logs, file, indent=4)
    else:
        with open(log_file_path, 'w') as file:
            json.dump([log_entry], file, indent=4)

# Connect to SQLite database and get the recipe
def get_recipe():
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        return "Do you remember this old recipe? \n\n" + SQL_utilities.random_recipe(cursor)
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        log_run("FAILED", f"Database connection failed: {e}")
        sys.exit(1)

### Communication with Telegram ###
# Load the .env file
if not load_dotenv(dotenv_path=f'{dir}/.env'):
    logging.error(".env file loading failed")
    log_run("FAILED", ".env file loading failed")
    sys.exit(1)

# Get the token and chat ID from environment variables
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

if not bot_token or not chat_id:
    logging.error("Bot token or chat ID is missing in .env")
    log_run("FAILED", "Bot token or chat ID is missing in .env")
    sys.exit(1)

# Initialize logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to send the message
async def send_initial_message():
    try:
        bot = Bot(token=bot_token)
        recipe_message = get_recipe()
        await bot.send_message(chat_id=chat_id, text=recipe_message)
        logging.info(f"Message sent to chat ID {chat_id}")
        log_run("SUCCESS", f"Message sent to chat ID {chat_id}")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")
        log_run("FAILED", f"Failed to send message: {e}")

# Main function
if __name__ == "__main__":
    if already_ran_today():
        logging.info("Script already ran today, skipping...")
        log_run("SKIPPED", "Script already ran today")
    else:
        asyncio.run(send_initial_message())