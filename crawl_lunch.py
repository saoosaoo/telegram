from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date


def crawl_lunch():
    # 실제로 오늘의 메뉴를 알아보고 싶다면 today = date.today() 로 바꾸어주세요.
    today = date(2020, 8, 31)

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    driver.get("https://school.iamservice.net/organization/17872/group/2076783")
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    menus = soup.select("#fe-contents > div > div.newsBoyd")
    for menu in menus:
        today_date = menu.select("h1")[0].text[:-5]
        if today_date == f'{today.month}월 {today.day}일':
            today_menu = "\n".join(list(menu.select("p.txt")[0].stripped_strings))
            return today_date, today_menu

if __name__ == "__main__":
    print(crawl_lunch()[1])