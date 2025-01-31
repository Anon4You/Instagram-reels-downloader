```markdown
# Instagram Reel Downloader Bot

This is a Telegram bot that allows users to download Instagram reels by simply providing the URL of the reel. The bot utilizes the `instaloader` library to fetch and download the video content.

## Features

- Download Instagram reels by sending the reel URL.
- Provides feedback to users during the download process.
- Automatically removes downloaded files after sending them to the user.
- Credits the original creator in the sent video caption.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Anon4You/Instagram-reel-downloader.git
   cd Instagram-reel-downloader
   ```

2. Install the required packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `token.txt` file in the project directory and add your Telegram bot token to it. The file should contain only the token, with no extra spaces or newlines.

4. Run the bot:

   ```bash
   python bot.py
   ```

## Usage

1. Start a chat with your bot on Telegram.
2. Send the command `/start` to initialize the bot.
3. Provide the URL of the Instagram reel you want to download.
4. The bot will respond with the downloaded video.

## Error Handling

The bot includes error handling for various issues that may arise during the download process, such as invalid URLs or network issues. Users will receive informative messages if something goes wrong.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [instaloader](https://github.com/instaloader/instaloader) - for downloading Instagram content.
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - for interacting with the Telegram Bot API.
- [BotFather](https://core.telegram.org/bots#botfather) - for creating Telegram bots.
```
