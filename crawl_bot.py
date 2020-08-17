from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler
from crawl_lunch import crawl_lunch


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="급식을 알고 싶으면 '머얌'이라고 물어봐!")

def reply_message(update, context):
    message = update.message.text
    if message == "머얌":
        date, menu = crawl_lunch()
        context.bot.send_message(chat_id=update.effective_chat.id, text= f'{date}\n\n{menu}')


if __name__ == "__main__":
    with open("token.txt", "r") as f:
        token = f.readline()
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), reply_message)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()