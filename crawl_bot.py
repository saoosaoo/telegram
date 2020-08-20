from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler
from crawl_lunch import crawl_lunch
from download_music import download_music, search_music
from file_uploader import Upload_file


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="급식을 알고 싶으면 '머얌'이라고 물어봐!")

def reply_message(update, context):
    message = update.message.text
    if message == "머얌":
        date, menu = crawl_lunch()
        context.bot.send_message(chat_id=update.effective_chat.id, text= f'{date}\n\n{menu}')

def music_download(update, context):
    music = ' '. join(context.args)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{music}을/를 다운로드 합니다.")
    url = search_music(music)
    context.bot.send_message(chat_id=update.effective_chat.id, text=url)
    file_path = download_music(music, url)
    Upload_file(file_path)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"구글 드라이브에 다운로드 완료!")


if __name__ == "__main__":
    with open("token.txt", "r") as f:
        token = f.readline()
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), reply_message)
    dispatcher.add_handler(echo_handler)

    download_handler = CommandHandler('m', music_download)
    dispatcher.add_handler(download_handler)

    updater.start_polling()