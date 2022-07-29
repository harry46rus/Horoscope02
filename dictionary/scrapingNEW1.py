import requests
import re
import time

import os
import random
import json
from bs4 import BeautifulSoup
import schedule
import pickle
import datetime

header = {'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


list_item = []
# def parss(key_):

now = datetime.datetime.now()
def scrap_news():

    def convert(timer):
        day_ = None

        if 'Вчера' in timer:
            day_ = datetime.datetime.now() - datetime.timedelta(days=1)
            ddd = f'{str(day_)[:10]} {timer[-5:]}'
            # print('1',ddd)
            sec = int(time.mktime(time.strptime(ddd, '%Y-%m-%d %H:%M')))
            hours_ = timer[-5:]
            # print(timer, sec, hours_)

        if 'Сегодня' in timer:
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

        return  sec, hours_

# ==================================================================

    link = "https://kurskcity.ru/news/main"

    resp = requests.get(link, headers=header)
    print(resp.status_code,'kurskcity.ru')
        # resp.raise_for_status()
    #     for i in range(58):
    #         try:
    news_dict={}
    news_list=[]

    soup = BeautifulSoup(resp.text, 'lxml')
    for i in range(16):
        News4 = soup.find_all('div', class_="container-fluid")#[i].find('h3').text
        News5 = soup.find_all('div', id="list_news_bl")#.find_all('a').text
        News6 = soup.find_all('div', class_="col-md-3 thumbnail row-flex")[i].find('a',
                        class_="black_link").text
        News7 = soup.find_all('div', class_="post-inner")[i].find('a').get('href')
        reff = 'https://kurskcity.ru' + News7
        time_iss = soup.find_all('div', class_="mainnewsdate small bltext")[i].text
        news_dict[News6] = [convert(time_iss),time_iss, reff,'www.kurskcity.ru']
        # print(News6," ",reff)
    #     news_list = list(news_dict)
    # print(news_dict)
    # print()
    # for j in range (16):
    #     print(news_list[j],news_dict[news_list[j]])
     # ===============================================
    # link = "http://www.dddkursk.ru/"
    #
    # resp = requests.get(link, headers=header)
    # print(resp.status_code)
    #
    # news_list = []
    #
    # soup = BeautifulSoup(resp.text, 'lxml')
    # # News_4 = soup.find_all('td', class_="right")
    # day_1 = soup.find_all('ul', class_="lenta")[0].find('nobr').text
    #
    # for y in range(25):
    #     try:
    #         News_4 = soup.find_all('ul', class_="lenta")[0].find_all('li')[y + 1].find('span').text
    #         News_5 = soup.find_all('ul', class_="lenta")[0].find_all('li')[0]  # .find('span')#.text
    #         time_ = f'{day_1} {News_4}'
    #         News40 = soup.find_all('ul', class_="lenta")[0].find_all('a')[y]  # .text#.get('href')
    #         News41 = News40.text
    #         News42 = "http://www.dddkursk.ru" + News40.get('href')
    #         # print(News41, News42)
    #         # print(News_4)
    #         news_dict[News41] = [convert(time_),time_, News42]
    #     # print('x=',News_4)
    #     except:
    #         break
    # =====================================================================/
    link = "https://www.46tv.ru/odnoj-strokoj/v-kurske/"

    resp = requests.get(link, headers=header)
    print(resp.status_code,'46tv.ru')

    news_list = []

    soup = BeautifulSoup(resp.text, 'lxml')
    # News_4 = soup.find_all('td', class_="right")
    # News_4 = soup.find_all('ul', class_="lenta")[0]
    for y in range(40):
        try:
            News40 = soup.find_all('div', id="dle-content")[0].find_all('div',
            class_="shortstory__content")[y].find('a')
            time_ = soup.find_all('div', id="dle-content")[0].find_all('div',
            class_="article-info__date")[y].text
            News41 = News40.text
            News42 = News40.get('href')
            #         print(News41,News42)
            #         # print(News40)
            news_dict[News41] = [convert(time_),time_, News42,'www.46tv.ru']
        except:
            print('46tv.ru')
            break
    # ======================================================
    pages_site = ['', '/page/2', '/page/3', '/page/4', '/page/5', '/page/6', '/page/7', '/page/8']
    for x in pages_site:
        link = "https://seyminfo.ru/news" + x

        resp = requests.get(link, headers=header)
        print(resp.status_code,'seyminfo.ru')

        news_list = []

        soup = BeautifulSoup(resp.text, 'lxml')
        # News_4 = soup.find_all('td', class_="right")
        # News_4 = soup.find_all('ul', class_="lenta")[0]
        for y in range(20):
            try:
                News40 =soup.find_all('div', class_="container content-container")[0].find_all('div',
                class_="card-body")[y]  # .find('a')
                time_ =soup.find_all('div', class_="container content-container")[0].find_all('div',
                class_="card-body")[y].find('span').text
                News42 = News40.find('a').get('href')
                News41 = News40.find('a').text
                # print(News41, News42)
                # print(News40)
                news_dict[News41] = [convert(time_),time_, News42,'www.seyminfo.ru']
            except:
                break
# ===============================================
    pages_site = ['', '?page=2', '?page=3']  # ,'?page=4','?page=5','?page=6','?page=7','?page=8']
    for x in pages_site:

        link = "https://kursk-izvestia.ru/news" + x
        # https://kursk-izvestia.ru/news?page=2

        resp = requests.get(link, headers=header)
        print(resp.status_code,'kursk-izvestia.ru')

        news_list = []

        soup = BeautifulSoup(resp.text, 'lxml')
        for i in range(32):
            try:
                News2 = soup.find_all('div', class_="blleft")[0].find_all('div', class_="created")[
                    i].text
                News3 = soup.find_all('div', class_="blleft")[0].find_all('div', class_="title")[
                    i].text
                News4 = soup.find_all('div', class_="blleft")[0].find_all('div', class_="title")[
                    i].find(
                    'a').get('href')
                reff = "https://kursk-izvestia.ru" + News4
                # print(News2,News3,reff)
                time_ = f'{News2[:12]}{News2[-6:]}'

                news_dict[News3] = [convert(time_), time_, reff,'www.kursk-izvestia.ru']

            except:
                print('kursk-izvestia.ru')
                break
# ==============================================
    link = "http://www.dddkursk.ru/lenta/"

    resp = requests.get(link, headers=header)
    print(resp.status_code,'dddkursk.ru')

    news_list = []

    soup = BeautifulSoup(resp.text, 'lxml')

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
            news_dict[News_5] = [convert(time_), time_, reff,'www.dddkursk.ru']

        except:
            break

    # =============================================
    def sorted_dicts(news_dict):
        sorted_dict = {}
        sorted_keys = sorted(news_dict, key=news_dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = news_dict[w]

        print('количество новостей = ',len(sorted_dict))
        return sorted_dict

    return sorted_dicts(news_dict) #news_dict
    # return news_dict

# def pick_date(sorted_dict):  # , shoplistfile):
#
#     """Запись  словаря в бинарный файл для хранения """
#     global dict2file
#     dict2file = 'Packnews.data'
#
#     f = open(dict2file, 'wb')  # 'wb')
#     pickle.dump(sorted_dict, f)  # помещаем объект в файл
#     f.close()
#
#     return dict2file#'Packnews.data'
#
#
#
# # Запись в файл
# pack_dict = pick_date(scrap())
#
# # Чтение в файла(распаковка)
# f = open(pack_dict, 'rb')
# base = pickle.load(f)
#
# print(base)
# print(dict2file)
# ==============================================
# def json_date(sorted_dict):
#
#     with open('news_bd8.json', 'w',encoding = 'utf-8') as file:
#         json.dumps(sorted_dict, indent=1, ensure_ascii=False)
#
#     path = "news_bd8.json"
#     with open(path, 'r', encoding = 'utf-8') as f_five:
#         json_data_news = json.load(f_five)
#
#     return json_data_news
# =============================================================
def json_date(sorted_dict):

    with open('news_bd8.json', 'w', encoding ='utf-8') as file:
        json.dump(sorted_dict, file, ensure_ascii=False, indent=0)


json_date(scrap_news())


def scrap():
    path = "news_bd8.json"
    with open(path, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    return json_data_news


# print(pack_dict)




# with open(path, 'r') as f_five:
#     json_data = json.load(f_five)
#
# for k in list(json_data.keys()):  # Для облегчения удаления данных при обходе словаря
#     if k == '002':
#         print("Загрузка прошла успешно")
#     json_data.pop(k)
# json_data = json.dumps(json_data，indent = 4)
#
# with open('F:\\wind data\\fail.json', 'a') as f_six:
#     f_six.write(json_data)


# dict={'01':1, '02':6, '03':19}
#
#
#
#
#
#
# print(json_data)
