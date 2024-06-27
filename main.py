from telegram_bot import TelegramBot



def on_user_contact(bot, update):

    if update.message.chat_id not in james.ADMINS:
        james.ADMINS.append(update.message.chat_id)
        print("new user contact! name: " + update.message.from_user.first_name)


def on_bell_ring():
    james.notify_users()


def on_open_request(bot, update):
    print(update.message.from_user.first_name + " tried unlocking the door")
    pass
    #if update.message.chat_id in james.ADMINS:
    #open_door();



if __name__ == "__main__":
    james = TelegramBot("")
    james.add_handler("open", on_open_request)
    james.add_handler("start", on_user_contact)
    james.start()
