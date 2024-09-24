#!/data/data/com.termux/files/usr/bin/python3

import time
import datetime
import asyncio
import logging
from dotenv import load_dotenv
from telegram import Bot
import os

# Link to my repo
dir = '/storage/emulated/0/MHDM_git'

# Start date and reminder frequency
start_date = datetime.date(2024, 9, 16)  # Replace with the actual start date
reminder_frequency = 3.5  # 2 pills per week (every 3.5 days)
total_weeks = 7

def send_reminder(week):
    return f"Reminder: Week {week} - Take your vitamin D pill today!"

def final_reminder():
    return "! All filled up in vitamin D !" + "\n" + "Remember to call the GP."
    

def main():
    current_date = datetime.date.today()
    days_passed = (current_date - start_date).days
    current_week = days_passed // 7 + 1
    
    if current_week > total_weeks:
        return final_reminder()
    else:
        # Check if it's a reminder day (every 3.5 days)
        if days_passed % 3.5 == 0:
            return send_reminder(current_week)
            
#!/data/data/com.termux/files/usr/bin/python3

import time
import datetime
import asyncio
import logging
from dotenv import load_dotenv
from telegram import Bot
import os

# Link to my repo
dir = '/storage/emulated/0/MHDM_git'

# Start date and reminder frequency
start_date = datetime.date(2024, 9, 16)  # Replace with the actual start date
reminder_frequency = datetime.timedelta(days=3.5)  # 2 pills per week (every 3.5 days)
total_weeks = 7

def send_reminder(week):
    return f"Reminder: Week {week} - Take your vitamin D pill today!"

def final_reminder():
    return "! All filled up in vitamin D !" + "\n" + "Remember to call the GP."
    
def main():
    current_date = datetime.date.today()
    days_passed = (current_date - start_date).days
    current_week = days_passed // 7 + 1

    if current_week > total_weeks:
        return final_reminder()
    else:
        # Check if today is a reminder day by comparing to start_date
        days_since_last_reminder = (current_date - start_date) % reminder_frequency
        if days_since_last_reminder == datetime.timedelta(0):
            return send_reminder(current_week)
    return None

if __name__ == "__main__":
    message = main()
    if message:
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
            await bot.send_message(chat_id=chat_id, text=message)
            logging.info(f"Message sent to chat ID {chat_id}")

        # Main function
        if bot_token and chat_id:
            asyncio.run(send_initial_message())
        else:
            logging.error("Bot token or chat ID is not set")
