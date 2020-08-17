import requests
from bs4 import BeautifulSoup


def get_training_data():
    res = requests.get('https://www.seti.go.kr/homepage/educourse/eduCourseList.go?menuId=1000000742&searchCnd=&searchGubun=02&searchYear=&searchMonth=&choiseMenu=00&searchTraInstId=')
    html = res.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('tbody > tr > td > ul > li > a')


    msg = ""
    for title in titles:
        msg = msg + title.text + "\n"

    print(msg)