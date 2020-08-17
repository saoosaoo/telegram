import schedule
import time
from crawl_lunch import crawl_lunch
import telegram

def job():
    print("I'm working...")
    date, menu = crawl_lunch()
    with open("token.txt", 'r') as f:
        token = f.readline()
    bot = telegram.Bot(token=token)
    bot.send_message(chat_id= "1366377962", text= f'{date}\n\n{menu}')


# 평일 아침 8:30마다 job 함수를 실행합니다
schedule.every().monday.at("8:30").do(job)
schedule.every().tuesday.at("8:30").do(job)
schedule.every().wednesday.at("8:30").do(job)
schedule.every().thursday.at("8:30").do(job)
schedule.every().friday.at("8:30").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)