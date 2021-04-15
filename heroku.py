import sys
import logging
from decouple import config
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)


API_KEY = config("TOKEN")
"""Bot token obtained from @BotFather on Telegram."""
URL = config("URL", None)
"""App url on deployment server like https://app-name.herokuapp.com/."""
PORT = config("PORT", 5000)
"""PORT assigned by hosting server."""
OWNER_ID = config("ID")
"""Give your own USERID"""
SPAMWATCH = config("SPAMWATCH")
"""give your spamwatch api"""
OWNER_USERNAME = config("OWNER_USERNAME")
"""give your own username"""
HEROKU_API_KEY = config("HEROKU_API_KEY")
"""Required for updating the bot and other stuff get it from https://dashboard.heroku.com/account"""
MESSAGE_DUMP = config("MESSAGE_DUMP")
"""Add group id where you want all messages get forwaded from your bot"""
HEROKU_APP_NAME = cofig("HEROKU_APP_NAME")
"""YOUR app name"""
SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")
"""YOUR SQL database url"""
LOAD = config("LOAD")
"""no load"""
NO_LOAD = config("O_LOAD")
"""features you don't want to load in app"""
WEHBOOK = config("WEHBOOK", false)
"""false"""
SUPPORT_USERS = config("SUPPORT_USERS")
"""List of id's (not usernames) for users which are allowed to gban, but can also be banned"""
WHITELIST_USERS = config("WHITELIST_USERS")
"""List of id's (not usernames) for users which WONT be banned/kicked by the bot"""
DONATION_LINK = config("DONATION_LINK")
"""EG, paypal"""
CERT_PATH = config("CERT_PATH", None)
"""Keep it none"""
DEL_CMDS = config("DEL_CMDS", false)
"""Whether or not you should delete 'blue text must click' commands"""
STRICT_GBAN = config("STRICT_GBAN", false)
"""put true or false"""
WORKERS = config("WORKERS", false)
"""no. of subthread to use"""
SUDO_USERS = config("SUDO_USERS")
"""Userid of users you want to keep in sudo"""


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    """/start command handler."""
    context.bot.send_message(
        update.message.chat_id,
        "STARTING JIVA.........", 
    )


def ping_pong(update, context):
    """ping message handler."""
    if update.message.text.lower() == "ping":
        context.bot.send_message(update.message.chat_id, "Ponggg!!!!")
    elif update.message.text.lower() == "pong":
        context.bot.send_message(update.message.chat_id, "Pingg!!!")


def main():
    """main function."""
    print("Starting Bot")
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    ping_pong_handler = MessageHandler(Filters.text & (~Filters.command), ping_pong)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_pong_handler)
    if len(sys.argv) > 1 and sys.argv[1] == "-l":
        print("Starting updater.")
        updater.start_polling()
    else:
        updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=API_KEY)
        print("Starting webhook.")
        updater.bot.setWebhook(URL + API_KEY)
    print("Bot has been started.")
    updater.idle()


if __name__ == "__main__":
    main()
