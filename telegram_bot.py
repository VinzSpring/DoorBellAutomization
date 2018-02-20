from telegram import Bot
from telegram.ext import Updater, CommandHandler


class TelegramBot:

    def __init__(self, API_TOKEN):
        self.API_TOKEN = API_TOKEN
        self.updater = Updater(self.API_TOKEN)
        self.bot = Bot(self.API_TOKEN)
        self.ADMINS = []

    def start(self):
        self.updater.start_polling()
        self.updater.idle()

    def stop(self):
        self.updater.stop()

    def add_handler(self, hot_phrase, callback):
        #TODO:add shortcut to telegram
        self.updater.dispatcher.add_handler(CommandHandler(hot_phrase, callback))

    def remove_handler(self, hot_phrase):
        try:
            del self.updater.dispatcher.handlers[hot_phrase]
        except LookupError:
            print("element " + str(hot_phrase) + " doesn't exist.")

    def notify_users(self):
        for admin in self.ADMINS:
            self.bot.send_message(chat_id=admin, text="I'm sorry Dave I'm afraid I can't do that.")
