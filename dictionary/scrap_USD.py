import json
import os
import threading
import time
from time import sleep
import requests
import datetime
# import re
# import time
# from time import sleep
# import os
# import random
# import json
from bs4 import BeautifulSoup
# import schedule
# import pickle
# import datetime
# import threading


header = {'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

# ===============================================
def scrap_USD():
    dict_USD={}
    link = "https://www.cbr.ru/currency_base/daily/"
    """USD"""
    # try:
    resp = requests.get(link, headers=header)
    print(resp.status_code,'info.ru')
    # except:
    #     print(resp.status_code, 'info.ru')
    news_list = []

    soup = BeautifulSoup(resp.text, 'lxml')
    # News_4 = soup.find_all('td', class_="right")
    # News_4 = soup.find_all('ul', class_="lenta")[0]
    News30 = soup.find_all('button', class_="datepicker-filter_button")[0].text
    try:

        News40 =soup.find_all('div', class_="table-wrapper")[0].find('tbody').find_all('tr')\
           [11].find_all('td')[3].text
        News41 = soup.find_all('div', class_="table-wrapper")[0].find('tbody').find_all('tr') \
            [11].find_all('td')[4].text
        News42 = soup.find_all('div', class_="table-wrapper")[0].find('tbody').find_all('tr') \
            [12].find_all('td')[3].text
        News43 = soup.find_all('div', class_="table-wrapper")[0].find('tbody').find_all('tr') \
            [12].find_all('td')[4].text
        # class_="card-body")[y]  # .find('a')
        # time_ =soup.find_all('div', class_="container content-container")[0].find_all('div',
        # class_="card-body")[y].find('span').text
        # News42 = News40.find('a').get('href')
        # News41 = News40.find('a').text
        # # print(News41, News42)
        # # print(News40)
        # news_dict[News41] = [convert(time_),time_, News42,'www.seyminfo.ru']
        print(News30)
        print(News40,News41)
        print(News42,News43,)
        dict_USD[News30] = [News40,News41,News42,News43]
    except:
        pass
    return dict_USD
# ====================================================


# scrap_USD()

def json_date(dict_USD):
    """Запись словаря с данными после парсера в json-файл. Наименование файла - секунды с начала
    эпохи"""
    #Определение  секунды сначала эпохи для текущего момента(для именование файла)
    ddday = str(datetime.datetime.now())[:16]
    print(ddday)
    sec = int(time.mktime(time.strptime(ddday, '%Y-%m-%d %H:%M')))
    print('sec', sec)
    print(time.ctime(sec))#Обратный преревод секунд в дату для контроля

    # path = f"bd_json\\news_bd8.json"

    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\USD_json\\{sec}_USD.json"

    # sorted_dict={'01':1, '02':6, '03':sec}

    with open(path1, 'w', encoding ='utf-8') as file:
        json.dump(dict_USD, file, ensure_ascii=False, indent=0)



def get_USD():
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""
    fild_bd = []
    #Перебор всех имен файлов в папке и запись в список имен
    for root, directory, file in os.walk(
            'C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\USD_json'):
        # print(root)
        # print(directory)
        for file_bd in file:
            fild_bd.append(file_bd)
    # Выборка позднего json-файла для показа на сайте
    print(max(fild_bd))
    #конвертация в обычный словарь
    path2=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\USD_json\\{max(fild_bd)}"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    print(json_data_news)
    return json_data_news

def loop_serv():
    """запуск скрипта (парсера) по расписанию указанному в листе  'time_scrap' """
    while True:
        time_scrap = ['00:03', '00:20', '00:40', '01:28','01:30',
                      '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45',
                      '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45',
                      '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
                      '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45',
                      '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45',
                      '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45',
                      '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45',
                      '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45',
                      '23:00', '23:20', '23:40',
                      ]
        delta_list=[]

        for hour_mins in time_scrap:
            print()
            full_date=f'{str(datetime.datetime.now())[:10]} {hour_mins}'
            secs = int(time.mktime(time.strptime(full_date, '%Y-%m-%d %H:%M')))

            ddday = str(datetime.datetime.now())[:16]
            # print(ddday)
            sec0 = int(time.mktime(time.strptime(ddday, '%Y-%m-%d %H:%M')))
            # print('sec0', sec0)

            delta=secs-sec0
            delta_list.append(delta)
            # print('delta', delta)
            #Если дата еще не наступила, то ждет ближайщую дату и запускает скрипт, потом дальще
            # повторяется все
            print('not start  of the parser')
            if delta > 0:
                sleep(delta)

                print('start  of the parser')
                json_date(scrap_USD())
                # get_USD()
                # scrap_USD()

# print(scrap())

# loop_serv()
# json_date(scrap_news())
# подключение функции скрапинга вторым потоком, иначе не запускается сервер
# t = threading.Thread(target=loop_serv)
# t.start()
# get_USD()