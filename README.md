# Telegram Bot Setup Instructions

## Overview

This guide will help you set up a Telegram bot that automatically reposts messages from one channel to another as new posts.

## Requirements

- A Telegram bot token (obtain from [BotFather](https://t.me/botfather))
- Admin access to both the source and target channels.
- A GitHub account.

## Step-by-Step Instructions

### 1. Set Up the Bot

- Create a bot using [BotFather](https://t.me/botfather) if you haven't done so yet.
- Copy the bot token provided by BotFather.

### 2. Add the Bot to Your Channels

- **Source Channel (SOURCE\_CHANNEL\_ID):**
  - Go to the settings of your source channel.
  - Select "Administrators" and add your bot as an administrator.
  - Grant the bot permission to view messages.
- **Target Channel (TARGET\_CHANNEL\_ID):**
  - Go to the settings of your target channel.
  - Select "Administrators" and add your bot as an administrator.
  - Grant the bot permission to post messages.

### 3. Configure the Script

- Update the following fields in the Python script:
  - `BOT_TOKEN` with your bot token.
  - `SOURCE_CHANNEL_ID` with the username of your source channel (e.g., `@source_channel`).
  - `TARGET_CHANNEL_ID` with the username of your target channel (e.g., `@target_channel`).

### 4. Run the Script

- Install the required Python library by running:
  ```sh
  pip install pyTelegramBotAPI
  ```
- Run the script:
  ```sh
  python your_script_name.py
  ```

## Notes

- The bot must have administrator rights in both channels to be able to repost messages.
- The bot will repost messages as new posts rather than as forwarded messages.

## Troubleshooting

- Ensure that the bot has the correct permissions in both channels.
- Make sure that you are using the correct `SOURCE_CHANNEL_ID` and `TARGET_CHANNEL_ID`.
- If the bot isn't working as expected, check the bot's logs for error messages.

Feel free to reach out if you need further assistance!

