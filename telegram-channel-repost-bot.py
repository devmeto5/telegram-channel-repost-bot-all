import telebot
from telebot import types

# Bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
# Source channel ID from which messages are copied
SOURCE_CHANNEL_ID = "@source_channel"
# Target channel ID where messages are posted
TARGET_CHANNEL_ID = "@target_channel"

bot = telebot.TeleBot(BOT_TOKEN)

# Handler for all incoming messages
@bot.channel_post_handler(func=lambda message: True)
def repost_message(message):
    # Check if the message is from the source channel
    if message.chat.username == SOURCE_CHANNEL_ID.replace("@", ""):
        # Post the message in the target channel as a new message
        if message.content_type == 'text':
            bot.send_message(TARGET_CHANNEL_ID, message.text)
        elif message.content_type == 'photo':
            bot.send_photo(TARGET_CHANNEL_ID, message.photo[-1].file_id, caption=message.caption)
        elif message.content_type == 'video':
            bot.send_video(TARGET_CHANNEL_ID, message.video.file_id, caption=message.caption)
        elif message.content_type == 'document':
            bot.send_document(TARGET_CHANNEL_ID, message.document.file_id, caption=message.caption)
        # Add handling for other types of messages if needed

if __name__ == "__main__":
    bot.polling(none_stop=True)