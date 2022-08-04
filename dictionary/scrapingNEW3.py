import requests
import re
import time
from time import sleep
import os
import random
import json
from bs4 import BeautifulSoup
import schedule
import pickle
import datetime
import threading

def scrap():
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""
    # fild_bd = []
    # #Перебор всех имен файлов в папке и запись в список имен
    # for root, directory, file in os.walk(
    #         'C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json'):
    #     # print(root)
    #     # print(directory)
    #     for file_bd in file:
    #         fild_bd.append(file_bd)
    # # Выборка позднего json-файла для показа на сайте
    # print(max(fild_bd))
    # #чтение и конвертация в обычный словарь
    path2=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    return json_data_news


def scrap1():
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""

    # #чтение и конвертация в обычный словарь
    path2=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    dict_1day_ago = {}

    # сделать словарь от начала дня 1дeн назад (вчера,) до Настоящего
    # времени

    # Определение  секунды сначала эпохи для начала текущего дня
    ddday = str(datetime.datetime.now())[:10]
    print(ddday)
    today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
    # Определение  секунды сначала эпохи для начала  дня 3дня назад (вчера, позавчера, поза-позавчера)
    start1d_ago = today_start_ #- 86400 * 1
    print("start1d_ago", start1d_ago)
    # print('yesterday_start_', today_start_ - 86400)
    # исключение данных ранее даты start3d_ago
    for j, i in json_data_news.items():
        # print(j,"___",i)
        if start1d_ago <= i[0]:
            # print(j, "___", i)
            dict_1day_ago[j] = i

    # print("3", dict_1day_ago)
    return dict_1day_ago


def scrap2():
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""

    # #чтение и конвертация в обычный словарь
    path2=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    dict_1day_ago = {}

    # сделать словарь от начала дня 1дeн назад (вчера,) до Настоящего
    # времени

    # Определение  секунды сначала эпохи для начала текущего дня
    ddday = str(datetime.datetime.now())[:10]
    print(ddday)
    today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
    # Определение  секунды сначала эпохи для начала  дня 3дня назад (вчера, позавчера, поза-позавчера)
    start1d_ago = today_start_ - 86400 * 1
    print("start1d_ago", start1d_ago)
    # print('yesterday_start_', today_start_ - 86400)
    # исключение данных ранее даты start3d_ago
    for j, i in json_data_news.items():
        # print(j,"___",i)
        if start1d_ago <= i[0]<=today_start_:
            # print(j, "___", i)
            dict_1day_ago[j] = i

    # print("3", dict_1day_ago)
    return dict_1day_ago








header = {'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}


list_item = []
# def parss(key_):
iterat_ = 1
now = datetime.datetime.now()
def scrap_news():




    global iterat_
    def convert(timer):
        """конвертация даты  сайта-источника и приведение (конвертация) к стандртному виду"""
        day_ = None
        global iterat_

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
    """дата в формате ( 16 июля 2022 года, 22:03)"""
    try:
        resp = requests.get(link, headers=header)
        print(resp.status_code,'kurskcity.ru')
    except:
        print(resp.status_code, 'kurskcity.ru')
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
        news_dict[News6] = [convert(time_iss)[0],convert(time_iss)[1],time_iss, reff,
                            'www.kurskcity.ru']
        # print(News6," ",reff)
    #     news_list = list(news_dict)
    # print(news_dict)
    # print()
    # for j in range (16):
    #     print(news_list[j],news_dict[news_list[j]])
#      # ===============================================
#
#     # =====================================================================/
    link = "https://www.46tv.ru/odnoj-strokoj/v-kurske/"
    """дата в формате  (Сегодня, 18: 51) """
    try:
        resp = requests.get(link, headers=header)
        print(resp.status_code,'46tv.ru')
    except:
        print(resp.status_code, '46tv.ru')
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
            news_dict[News41] = [convert(time_)[0],convert(time_)[1],time_, News42,'www.46tv.ru']
        except:
            # print('46tv.ru')
            break
#     # ======================================================

    if iterat_ == 0:
        pages_site = ['', '/page/2', '/page/3', '/page/4', '/page/5', '/page/6', '/page/7', '/page/8']
    else:
        pages_site = ['',]
    for x in pages_site:
        # sleep(20)
        link = "https://seyminfo.ru/news" + x
        """дата в формате   (23:28 16.07.2022)"""
        try:
            resp = requests.get(link, headers=header)
            print(resp.status_code,'seyminfo.ru')
        except:
            print(resp.status_code, 'seyminfo.ru')
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
                news_dict[News41] = [convert(time_)[0],convert(time_)[1],time_, News42,
                                     'www.seyminfo.ru']
            except:
                break
# # ===============================================
    if iterat_ == 0:
        pages_site = ['', '?page=2', '?page=3']  # ,'?page=4','?page=5','?page=6','?page=7','?page=8']
    else:
        pages_site = ['',]
    for x in pages_site:
        # sleep(20)
        link = "https://kursk-izvestia.ru/news" + x
        # https://kursk-izvestia.ru/news?page=2
        """дата в формате   (16 июля 2022 в 20:01)"""
        try:
            resp = requests.get(link, headers=header)
            print(resp.status_code,'kursk-izvestia.ru')
        except:
            print(resp.status_code, 'kursk-izvestia.ru')
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

                news_dict[News3] = [convert(time_)[0],convert(time_)[1], time_, reff,
                                    'www.kursk-izvestia.ru']

            except:
                print('kursk-izvestia.ru')
                break
# # ==============================================
    link = "http://www.dddkursk.ru/lenta/"
    """дата в формате   (16 июля 2022, 17:12)"""
    try:
        resp = requests.get(link, headers=header)
        print(resp.status_code,'dddkursk.ru')
    except:
        print(resp.status_code, 'dddkursk.ru')
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
            news_dict[News_5] = [convert(time_)[0],convert(time_)[1], time_, reff,'www.dddkursk.ru']

        except:
            break
    iterat_+= 1
#     print("iterat_",iterat_)
    # =============================================

#     news_dict={
# "«Металлоинвест» построил в Железногорске две новые спортплощадки": [[
# 1659347940,
# "12:59"
# ],
# "12:59 01.08.2022",
# "https://seyminfo.ru/metalloinvest-postroil-v-zheleznogorske-dve-novye-sportploshhadki.html",
# "www.seyminfo.ru"
# ],
# "В Курской области за неделю произошло 47 пожаров": [
# [
# 1659347520,
# "12:52"
# ],
# "01 августа 2 12:52",
# "https://kursk-izvestia.ru/news/187745/",
# "www.kursk-izvestia.ru"
# ],
# "В Курске за неделю составили 22 протокола из-за незаконной торговли": [
# [
# 1659347460,
# "12:51"
# ],
# "12:51 01.08.2022",
# "https://seyminfo.ru/v-kurske-za-nedelju-sostavili-22-protokola-iz-za-nezakonnoj-torgovli.html",
# "www.seyminfo.ru"
# ],
# "В Коренево Курской области женщину зажало между двумя автомобилями": [
# [
# 1659347220,
# "12:47"
# ],
# "Сегодня, 12:47",
# "https://46tv.ru/odnoj-strokoj/v-kurske/171726-v-korenevo-kurskoj-oblasti-zhenschinu-zazhalo-mezhdu-dvumja-avtomobiljami.html",
# "www.46tv.ru"
# ]}

    # =================================================

    def read_json():
        path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"

        with open(path2, 'r', encoding='utf-8') as f_five:
            json_data_news = json.load(f_five)
        print("1", json_data_news)
        return json_data_news

    def merge_dict(gen,add_):
        gen.update(add_)
        print("2", gen)
        dict_3day_ago = {}

        # сделать словарь от начала дня 3дня назад (вчера, позавчера, поза-позавчера) до Настоящего
        # времени

        # Определение  секунды сначала эпохи для начала текущего дня
        ddday = str(datetime.datetime.now())[:10]
        print(ddday)
        today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
        # Определение  секунды сначала эпохи для начала  дня 3дня назад (вчера, позавчера, поза-позавчера)
        start3d_ago = today_start_ - 86400*4
        print("start3d_ago", start3d_ago)
        # print('yesterday_start_', today_start_ - 86400)
        #исключение данных ранее даты start3d_ago
        for j, i in gen.items():
            # print(j,"___",i)
            if start3d_ago <= i[0]:
                # print(j, "___", i)
                dict_3day_ago[j] = i

        print("3", dict_3day_ago)
        return dict_3day_ago

    month_liter = {
        'Jan': 'января', 'Feb': 'февраля', 'Mar': 'марта', 'Apr': 'апреля', 'May': 'мая',
        'Jun': 'июня', 'Jul': 'июля', 'Aug': 'августа', 'Sep': 'сентября', 'Oct': 'октября',
        'Nov': 'ноября', 'Dec': 'декабря'}

    nal_dict = {}
    final_dict = {}
    def filter(json_data_news):
        for i, j in json_data_news.items():
            # print(i,"_____",j)
            nal_dict[j[3]] = [i, j[0], j[1], j[2], j[4]]
        for i, j in nal_dict.items():
            dtime = time.ctime(int(j[1])).split()
            day_time = f'{dtime[2]} {month_liter[dtime[1]]}'
            # print(i,"_____",j)
            final_dict[j[0]] = [j[1], j[2], day_time, i, j[4]]
            # final_dict[j[0]] = [j[1], j[2], j[3], i, j[4]]

        return final_dict
# ===================================================
#     for i,j in json_data_news.items():
#         # print(i,"_____",j)
#         nal_dict[j[3]]= [i,j[0],j[1],j[2],j[4]]
#
#     for i,j in nal_dict.items():
#         dtime = time.ctime(int(j[1])).split()
#         day_time = f'{dtime[2]} {month_liter[dtime[1]]}'
#
#         # print(i,"_____",j)
#         final_dict[j[0]]=[j[1],j[2],day_time,i,j[4]]
#         # final_dict[j[0]]=[j[1],j[2],j[3],i,j[4]]
#     # for i,j in final_dict.items():
#     #     print(i,"__",day_time,"__",j)
#     # return final_dict
#     return final_dict

# ==================================================
    def sorted_dicts(news_dict):
        """Сортировка словаря по дате элементов(новостей) """
        sorted_dict = {}
        sorted_keys = sorted(news_dict, key=news_dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = news_dict[w]
        count_news =len(sorted_dict)
        print('количество новостей = ', count_news)
        print(sorted_dict)
        return sorted_dict

    ddd=filter(merge_dict(read_json(), news_dict))
    print(ddd)
    dddd=sorted_dicts(ddd)
    print(dddd)
    return dddd

# =============================================================
# def json_date(sorted_dict):
#
#     with open('news_bd8.json', 'w', encoding ='utf-8') as file:
#         json.dump(sorted_dict, file, ensure_ascii=False, indent=0)
#
#
# json_date(scrap_news())
#
#
# def scrap():
#     path = "news_bd8.json"
#     with open(path, 'r', encoding='utf-8') as f_five:
#         json_data_news = json.load(f_five)
#
#     return json_data_news
#

# print(pack_dict)
# ========================================





def totaldate(date_dict):

    """Запись словаря с данными после парсера в GLdate.json json-файл."""

    path1=f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"

    with open(path1, 'w', encoding ='utf-8') as file:
        json.dump(date_dict, file, ensure_ascii=False, indent=0)

# print("x", scrap_news())
# totaldate(scrap_news())



# =======================================================

time_list0=['00:00', '00:20', '00:40', '01:00','01:33',
          '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45',
          '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45',
          '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
          '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45',
          '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45',
          '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45',
          '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45',
          '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45',
          '23:00', '23:20', '23:40'
          ]


def loop_serv(time_scrap):
    """запуск скрипта (парсера) по расписанию указанному в листе  'time_list0' """
    while True:

        def sec_count(hour_min_):
            """вычисляет количесто секунд  от начала эпохи до сегодняшнего любого
             момента в формате  21:25 часы:минуты """
            full_date = f'{str(datetime.datetime.now())[:10]} {hour_min_}'
            secs_ = int(time.mktime(time.strptime(full_date, '%Y-%m-%d %H:%M')))
            return secs_

        for hour_mins in time_scrap:
            print()
            print(f'Запуск в {hour_mins}')

            # print('secs',sec_count(hour_mins))

            ddday = str(datetime.datetime.now())[:16]
            print(ddday)
            sec0 = int(time.mktime(time.strptime(ddday, '%Y-%m-%d %H:%M')))
            # print('sec0', sec0)

            delta=sec_count(hour_mins)-sec0

            print(f'Ожидание {delta} секунд')
            #Если дата еще не наступила, то ждет ближайщую дату и запускает скрипт, потом дальще
            # повторяется все
            # print('not start==============')
            if delta > 0:
                sleep(delta)
#
                print('start  of the NEWS-PARSER-script')

                totaldate(scrap_news())

            elif time_scrap[-1] == hour_mins:
                delta1=86400-5-(sec_count(time_scrap[-1])-sec_count(time_scrap[0]))
                print(f'ожидание {delta1} секунд до {time_scrap[0]}')
                print(time_scrap[-1],time_scrap[0])
                print(sec_count(time_scrap[-1]),sec_count(time_scrap[0]))
                sleep(delta1)

# print(scrap())

# loop_serv()



# подключение функции скрапинга вторым потоком, иначе не запускается сервер
t = threading.Thread(target=loop_serv, args=(time_list0,))
t.start()


# ========================================

# def json_date(sorted_dict):
#     """Запись словаря с данными после парсера в json-файл. Наименование файла - секунды с начала
#     эпохи"""
#     #Определение  секунды сначала эпохи для текущего момента(для именование файла)
#     ddday = str(datetime.datetime.now())[:16]
#     print(ddday)
#     sec = int(time.mktime(time.strptime(ddday, '%Y-%m-%d %H:%M')))
#     print('sec', sec)
#     print(time.ctime(sec))#Обратный преревод секунд в дату для контроля
#
#     # path = f"bd_json\\news_bd8.json"
#
#     path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\{sec}.json"
#
#     # sorted_dict={'01':1, '02':6, '03':sec}
#
#     with open(path1, 'w', encoding ='utf-8') as file:
#         json.dump(sorted_dict, file, ensure_ascii=False, indent=0)