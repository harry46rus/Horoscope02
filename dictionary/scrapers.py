import requests
import re
import time
# from time import sleep
# import os
import json
from bs4 import BeautifulSoup
import datetime
import threading

header = {'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

list_item = []
# def parss(key_):
iterat_ = 1
now = datetime.datetime.now()

def convert(timer):
    """конвертация даты публикации сайта-источника и приведение (конвертация) к стандртному
    виду"""
    day_ = None
    global iterat_

    if 'вчера' in timer:
        day_ = datetime.datetime.now() - datetime.timedelta(days=1)
        ddd = f'{str(day_)[:10]} {timer[-5:]}'
        # print('1',ddd)
        sec = int(time.mktime(time.strptime(ddd, '%Y-%m-%d %H:%M')))
        hours_ = timer[-5:]
        # print(timer, sec, hours_)

    if 'сегодня' in timer:
        day_ = datetime.datetime.now()
        ddd = f'{str(day_)[:10]} {timer[-5:]}'
        # print('2',ddd)
        sec = int(time.mktime(time.strptime(ddd, '%Y-%m-%d %H:%M')))
        hours_ = timer[-5:]
        # print(timer, sec, hours_)
    try:
        sec = int(time.mktime(time.strptime(timer, '%H:%M %d.%m.%Y')))  # '11:14 04.07.2022'
        hours_ = timer[:5]
        # print(timer, sec, hours_)

    except:
        pass

    month_ = {
        '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля', '05': 'мая',
        '06': 'июня',
        '07': 'июля', '08': 'августа', '09': 'сентября', '10': 'октября', '11': 'ноября',
        '12': 'декабря'
    }

    for j in range(12):
        if month_[list(month_)[j]] in timer:
            number_month = list(month_)[j]
            # print(number_month)
            date_ = f'{str(now)[:4]}-{number_month}-{timer[:2]} {timer[-5:]}'
            # print(date_)
            sec = int(time.mktime(time.strptime(date_, '%Y-%m-%d %H:%M')))
            hours_ = timer[-5:]
            # print(timer, sec, hours_)

    try:
        sec = int(time.mktime(time.strptime(timer, '%Y-%m-%d %H:%M')))  # '11:14 04.07.2022'
        hours_ = timer[-5:]
        # print(timer, sec, hours_)

    except:
        pass

    return sec, hours_

# ==================================================================

def kurskcity():
    resp =None
    link = "https://kurskcity.ru/news/main"
    """дата в формате ( 16 июля 2022 года, 22:03)"""
    try:
        resp = requests.get(link, headers=header)
        soup = BeautifulSoup(resp.text, 'lxml')
        # print(resp.status_code, 'kurskcity.ru')
    except:
        pass
        print('ERROR-kurskcity.ru')
        # print(resp.status_code, 'kurskcity.ru')
        # resp.raise_for_status()
    #     for i in range(58):
    #         try:
    news_dict = {}
    news_list = []


    for i in range(16):
        try:
            News4 = soup.find_all('div', class_="container-fluid")  # [i].find('h3').text
            News5 = soup.find_all('div', id="list_news_bl")  # .find_all('a').text
            News6 = soup.find_all('div', class_="col-md-3 thumbnail row-flex")[i].find('a',
            class_="black_link").text
            News7 = soup.find_all('div', class_="post-inner")[i].find('a').get('href')
            reff = 'https://kurskcity.ru' + News7
            time_iss = soup.find_all('div', class_="mainnewsdate small bltext")[i].text
            news_dict[News6] = [convert(time_iss)[0], convert(time_iss)[1], time_iss, reff,
                                'www.kurskcity.ru']
            # print(News6," ",reff)
        #     news_list = list(news_dict)
        except:
            # print(f"=====ошибка скрапинга кода kurskcity.ru=====итераций_{y}=========")
            break
    return news_dict

# print(kurskcity())
# print(len(kurskcity()))

# print(news_dict)
# print()
# for j in range (16):
#     print(news_list[j],news_dict[news_list[j]])

# =======================================
def gtrkkursk():
    resp = None
    news_dict = {}
    page_site = ['', '?page=1']
    for x in page_site:
        link = "https://gtrkkursk.ru/news-list" + x

        """дата в формате ( чт, 4 августа 2022 - 17:22)"""
        try:
            resp = requests.get(link, headers=header)
            soup = BeautifulSoup(resp.text, 'lxml')
            # print(resp.status_code, 'gtrkkursk.ru')
        except:
            print('ERROR-gtrkkursk.ru')
            pass
            # print(resp.status_code, 'gtrkkursk.ru')
            # resp.raise_for_status()
        #     for i in range(58):
        #         try:

        news_list = []


        for i in range(12):
            try:
                News6 = soup.find('div', class_="view-content"  )
                News7 = News6.find_all('a' ,class_='item_pic-wrapper')[i].get('href')
                reff = 'https://gtrkkursk.ru/' + News7

                News8 = News6.find_all('h2' ,class_='title')[i].text#

                News9 = News6.find_all('span' ,class_='item_time')[i].text#
                time_iss = f'{News9[-23:-8]} {News9[-5:]}'

                news_dict[News8] = [convert(time_iss)[0], convert(time_iss)[1], time_iss, reff,
                                    'www.gtrkkursk.ru']
            except:
                pass
                # print("===========ошибка скрапинга кода gtrkkursk.ru=========================")
            # print('News7'," ",News7)
            # print('News8'," ",News8)
            # print('News9'," ",News9)
            # print('time_iss'," ",time_iss)
            # print('reff'," ",reff)
        #     news_list = list(news_dict)
    return news_dict

def s46tv():
    resp = None

    news_dict = {}
    link = "https://www.46tv.ru/odnoj-strokoj/v-kurske/"
    """дата в формате  (Сегодня, 18: 51) """
    try:
        resp = requests.get(link, headers=header)
        soup = BeautifulSoup(resp.text, 'lxml')
        # print(resp.status_code, '46tv.ru')
    except:
        print('ERROR-46tv.ru')
        # print(resp.status_code, '46tv.ru')
        pass
    news_list = []


    # News_4 = soup.find_all('td', class_="right")
    # News_4 = soup.find_all('ul', class_="lenta")[0]
    for y in range(40):
        try:
            News40 = soup.find_all('div', id="dle-content")[0].find_all('div',
            class_="shortstory__content")[y].find('a')
            time_ = soup.find_all('div', id="dle-content")[0].find_all('div',
            class_="article-info__date")[y].text
            time_ = time_.lower()
            News41 = News40.text
            News42 = News40.get('href')
            #         print(News41,News42)
            #         # print(News40)
            news_dict[News41] = [convert(time_)[0], convert(time_)[1], time_, News42,
                                 'www.46tv.ru']
        except:
            # print(f"=====ошибка скрапинга кода 46tv.ru=====итераций_{y}=========")
            break
    return news_dict

#     # ======================================================
def seyminfo():
    resp = None
    news_dict = {}
    global iterat_
    if iterat_ == 0:
        pages_site = ['', '/page/2', '/page/3', '/page/4', '/page/5', '/page/6', '/page/7',
                      '/page/8']
    else:
        pages_site = ['', ]
    for x in pages_site:
        # sleep(20)
        link = "https://seyminfo.ru/news" + x
        """дата в формате   (23:28 16.07.2022)"""
        try:
            resp = requests.get(link, headers=header)
            soup = BeautifulSoup(resp.text, 'lxml')
            # print(resp.status_code, 'seyminfo.ru')
        except:
            pass
            print('ERROR-seyminfo.ru')
            # print(resp.status_code, 'seyminfo.ru')
        news_list = []


        # News_4 = soup.find_all('td', class_="right")
        # News_4 = soup.find_all('ul', class_="lenta")[0]

        for y in range(20):
            try:
                News40 = \
                    soup.find_all('div', class_="container content-container")[0].find_all('div',
                    class_="card-body")[y]  # .find('a')
                time_ = \
                    soup.find_all('div', class_="container content-container")[0].find_all('div',
                    class_="card-body")[y].find('span').text
                News42 = News40.find('a').get('href')
                News41 = News40.find('a').text
                # print(News41, News42)
                # print(News40)
                news_dict[News41] = [convert(time_)[0], convert(time_)[1], time_, News42,
                                     'www.seyminfo.ru']
            except:
                # print(f"=====ошибка скрапинга кода seyminfo.ru=====итераций_{y}=========")
                break
    return news_dict

# # ===============================================
def k_izvestia():
    resp = None
    global iterat_
    news_dict = {}
    if iterat_ == 0:
        pages_site = ['', '?page=2',
                      '?page=3']  # ,'?page=4','?page=5','?page=6','?page=7','?page=8']
    else:
        pages_site = ['', ]
    for x in pages_site:
        # sleep(20)
        link = "https://kursk-izvestia.ru/news" + x
        # https://kursk-izvestia.ru/news?page=2
        """дата в формате   (16 июля 2022 в 20:01)"""
        try:
            resp = requests.get(link, headers=header)
            soup = BeautifulSoup(resp.text, 'lxml')
            # print(resp.status_code, 'kursk-izvestia.ru')
        except:
            print('ERROR-kursk-izvestia.ru')
            # print(resp.status_code, 'kursk-izvestia.ru')
            pass
        news_list = []


        for i in range(32):
            try:
                News2 = soup.find_all('div', class_="blleft")[0].find_all('div',
                        class_="created")[i].text
                News3 = soup.find_all('div', class_="blleft")[0].find_all('div',
                        class_="title")[i].text
                News4 = soup.find_all('div', class_="blleft")[0].find_all('div',
                        class_="title")[i].find('a').get('href')

                reff = "https://kursk-izvestia.ru" + News4
                # print(News2,News3,reff)
                time_ = f'{News2[:12]}{News2[-6:]}'

                news_dict[News3] = [convert(time_)[0], convert(time_)[1], time_, reff,
                                    'www.kursk-izvestia.ru']

            except:
                # print(f"=====ошибка скрапинга кода kursk-izvestia.ru=====итераций_{i}=========")
                break
    return news_dict

# # ==============================================
def dddkursk():
    resp = None
    news_dict = {}
    link = "http://www.dddkursk.ru/lenta/"
    """дата в формате   (16 июля 2022, 17:12)"""
    try:
        resp = requests.get(link, headers=header)
        soup = BeautifulSoup(resp.text, 'lxml')
        # print(resp.status_code, 'dddkursk.ru')
    except:
        print('ERROR-dddkursk.ru')
        # print(resp.status_code, 'dddkursk.ru')
        pass
    news_list = []



    for y in range(40):
        try:
            time_ = soup.find_all('td', class_="center")[1].find_all('nobr')[y].text
            News_4 = soup.find_all('td', class_="center")[1].find_all('h3')[y]
            News_5 = News_4.find('a').text
            News_6 = News_4.find('a').get('href')
            reff = "http://www.dddkursk.ru" + News_6
            # print(time_)
            # print(News_5)
            # print(reff)
            # print()
            # print()
            news_dict[News_5] = [convert(time_)[0], convert(time_)[1], time_, reff,
                                 'www.dddkursk.ru']

        except:
            print(f"=====ошибка скрапинга кода dddkursk.ru=====итераций_{y}=========")
            break
    return news_dict

#     print("iterat_",iterat_)

# ==========================================
def mchs():
    resp = None
    news_dict = {}
    link = "https://46.mchs.gov.ru/deyatelnost/press-centr/operativnaya-informaciya"
    """дата в формате   (29 августа 2022, 12:31)"""
    try:
        resp = requests.get(link, headers=header)
        soup = BeautifulSoup(resp.text, 'lxml')
    except:
        print('ERROR-mchs.gov.ru')
        # print(resp.status_code, 'mchs.gov.ru')
        pass
    news_list = []



    for y in range(10):
        try:
            time_ = soup.find('div', class_="main-content").find_all('span',
             class_="articles-item__date")[y].text


            # print(time_)
            title_ = soup.find('div', class_="main-content").find_all('a',
            class_="articles-item__title")[y].text


            # print(title_)
            reff = soup.find('div', class_="main-content").find_all('a',
            class_="articles-item__title")[y].get('href')


            reff = 'https://46.mchs.gov.ru' + reff
            # print(reff)

            news_dict[title_] = [convert(time_)[0], convert(time_)[1], time_, reff,
                                 'www.46.mchs.gov.ru']

        except:
            print(f"=====ошибка скрапинга кода mchs.gov.ru=====итераций_{y}=========")
            break
    return news_dict
# ==========================================

def mvd():
    resp = None

    news_dict = {}
    link = "https://46.мвд.рф/news"
    """дата в формате   (Сегодня  14:13, 26 Августа  12:39)"""

    try:
        resp = requests.get(link, headers=header)
        soup = BeautifulSoup(resp.text, 'lxml')
        print(resp.status_code, '46.мвд.рф')
    except:
        # print(resp.status_code, '46.мвд.рф')
        print( 'ERROR-46.мвд.рф')
        pass
    news_list = []



    for y in range(10):
        try:
            time_0 = soup.find('div', class_="b-news").find_all('div',
            class_="sl-item-date")[y].text[:]
            time_1 = (re.findall('\d?\d?\s?\w*', time_0))[0]
            print(time_1)
            # time_1 = soup.find('div', class_="b-news").find_all('div',
            #         class_="sl-item-date")[5].text
            time_2 = (re.findall('\d{2}:\d{2}', time_0))[0]
            print(time_2)
            time_ = f'{time_1.lower()} {time_2}'
            print(time_)
            title_ = soup.find('div', class_="b-news").find_all('div',
            class_="sl-item-title")[y].text
            print(title_)
            reff = soup.find('div', class_="b-news").find_all('div',
            class_="sl-item-title")[y].find('a').get('href')
            reff = 'https://46.мвд.рф' + reff
            print(reff)
            print(convert(time_)[0])
            print(convert(time_)[1])

            news_dict[title_.strip('\n')] = [convert(time_)[0], convert(time_)[1], time_, reff,
                                 'www.46.мвд.рф']
        except:
            print(f"=====ошибка чтения кода 46.мвд.рф=====итераций_{y}=========")
            break
    return news_dict
