#!/usr/bin/env python
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
#┃ Project : Instagram Reels Downloader Bot            ┃
#┃ Author  : Alienkrishn [Anon4You]                    ┃
#┃ Version : 1.0.0 (Latest)                            ┃  
#┃ Github  : github.com/Anon4You                       ┃
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
import telebot
import instaloader
import os
import glob
import shutil

def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

BOT_TOKEN = read_token_from_file('token.txt')
bot = telebot.TeleBot(BOT_TOKEN)
loader = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me an Instagram reel URL, and I'll download it for you.")

@bot.message_handler(func=lambda message: True)
def download_reel(message):
    url = message.text
    try:
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        if post.is_video:
            progress_msg = bot.reply_to(message, "Downloading your reel...")
            download_dir = shortcode
            loader.download_post(post, target=download_dir)

            video_files = glob.glob(os.path.join(download_dir, '*.mp4'))

            bot.delete_message(progress_msg.chat.id, progress_msg.message_id)

            caption = post.caption if post.caption else "No caption available."
            caption += "\n\nCreated by [Alienkrishn](https://github.com/Anon4You)"

            if video_files:
                video_file_path = video_files[0]

                with open(video_file_path, 'rb') as f:
                    bot.send_video(message.chat.id, f, caption=caption, parse_mode='Markdown')

                shutil.rmtree(download_dir)
            else:
                bot.reply_to(message, "Could not find the downloaded video file. Please try again.")

        else:
            bot.reply_to(message, "The provided URL is not a reel or video.")

    except instaloader.exceptions.InstaloaderException as e:
        bot.reply_to(message, f"An error occurred while downloading: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"An unexpected error occurred: {str(e)}")

bot.polling()
