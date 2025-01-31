#!/usr/bin/env python
import telebot
import instaloader
import os
import glob
import shutil

# Function to read the bot token from a file
def read_token_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Get the bot token from token.txt
BOT_TOKEN = read_token_from_file('token.txt')
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize Instaloader
loader = instaloader.Instaloader()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me an Instagram reel URL, and I'll download it for you.")

@bot.message_handler(func=lambda message: True)
def download_reel(message):
    url = message.text
    try:
        # Extract the shortcode from the URL
        shortcode = url.split("/")[-2]  # Assumes the URL is in the format https://www.instagram.com/reel/shortcode/
        
        # Load the post
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        if post.is_video:
            # Create a progress message
            progress_msg = bot.reply_to(message, "Downloading your reel...")

            # Download the video
            download_dir = shortcode
            loader.download_post(post, target=download_dir)  # Downloads to a folder named after the shortcode

            # Look for the downloaded video file
            video_files = glob.glob(os.path.join(download_dir, '*.mp4'))  # Get all .mp4 files in the directory

            # Remove the progress message
            bot.delete_message(progress_msg.chat.id, progress_msg.message_id)

            # Prepare the caption
            caption = post.caption if post.caption else "No caption available."
            # Add the credit line
            caption += "\n\nCreated by [Alienkrishn](https://github.com/Anon4You)"  # Markdown formatting for clickable link

            # Check if any video files were found
            if video_files:
                # Use the first found video file
                video_file_path = video_files[0]  

                # Send the video back to the user with the caption
                with open(video_file_path, 'rb') as f:
                    bot.send_video(message.chat.id, f, caption=caption, parse_mode='Markdown')

                # Clean up the downloaded files
                shutil.rmtree(download_dir)  # Remove the directory after sending
            else:
                bot.reply_to(message, "Could not find the downloaded video file. Please try again.")

        else:
            bot.reply_to(message, "The provided URL is not a reel or video.")

    except instaloader.exceptions.InstaloaderException as e:
        bot.reply_to(message, f"An error occurred while downloading: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"An unexpected error occurred: {str(e)}")

bot.polling()
