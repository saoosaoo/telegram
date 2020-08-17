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

i = "08:30"
# 평일 아침 8:30마다 job 함수를 실행합니다
schedule.every().tuesday.at(i).do(job)
schedule.every().monday.at(i).do(job)
schedule.every().wednesday.at(i).do(job)
schedule.every().thursday.at(i).do(job)
schedule.every().friday.at(i).do(job)


while True:
    schedule.run_pending()
    time.sleep(1)