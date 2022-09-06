import requests
import re
import time
# from time import sleep
# import os
# import random
import json
from bs4 import BeautifulSoup
import datetime
import threading
from scrapers import kurskcity,gtrkkursk,s46tv,seyminfo,k_izvestia,dddkursk,mchs,mvd
from taggers import anons, accidents,societ,jkh
from paths_01 import path_bd_json


header = {'Accept': '*/*',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
    (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

list_item = []
# def parss(key_):
iterat_ = 1
now = datetime.datetime.now()


def scrap_news():
    global iterat_


    # =============================================
    dict_total = {}
    list_scr = [dict_total, kurskcity(), gtrkkursk(), s46tv(), seyminfo(), k_izvestia(),
                dddkursk(), mchs(), mvd()]
    for i in range(len(list_scr) - 1):
        # merge_dict(list_scr[0], list_scr[i+1])
        list_scr[0].update(list_scr[i + 1])
    # print(list_scr[0])
    # print(len(list_scr[0]))
    iterat_ += 1

    # =================================================

    def read_json():

        path2 = f"{path_bd_json}GLdate0.json"
        # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"
        # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"
        with open(path2, 'r', encoding='utf-8') as f_five:
            json_data_news = json.load(f_five)
        # print("1", json_data_news)
        return json_data_news

    def merge_dict(gen, add_):
        gen.update(add_)
        # print("2", gen)
        dict_3day_ago = {}

        # сделать словарь от начала дня 3дня назад (вчера, позавчера, поза-позавчера) до Настоящего
        # времени

        # Определение  секунды сначала эпохи для начала текущего дня
        ddday = str(datetime.datetime.now())[:10]
        # print(ddday)
        today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
        # Определение  секунды сначала эпохи для начала  дня n-дня назад (вчера, позавчера,
        # поза-позавчера)
        start3d_ago = today_start_ - 86400 * 7
        # print("start3d_ago", start3d_ago)
        # print('yesterday_start_', today_start_ - 86400)
        # исключение данных ранее даты start3d_ago
        for j, i in gen.items():
            # print(j,"___",i)
            if start3d_ago <= i[0]:
                # print(j, "___", i)
                dict_3day_ago[j] = i

        # print("3", dict_3day_ago)
        return dict_3day_ago

    month_liter = {
        'Jan': 'января', 'Feb': 'февраля', 'Mar': 'марта', 'Apr': 'апреля', 'May': 'мая',
        'Jun': 'июня', 'Jul': 'июля', 'Aug': 'августа', 'Sep': 'сентября', 'Oct': 'октября',
        'Nov': 'ноября', 'Dec': 'декабря'}

    nal_dict = {}
    final_dict = {}

    def filter(json_data_news):
        """Удаляет дубли новостей которые получаются, когда редакции корректируют заголовок после
        выпуска"""
        for i, j in json_data_news.items():
            # print(i,"_____",j)
            nal_dict[j[3]] = [i, j[0], j[1], j[2], j[4]]

        for i, j in nal_dict.items():
            # print(i,j)
            dtime = time.ctime(int(j[1])).split()
            day_time = f'{dtime[2]} {month_liter[dtime[1]]}'
            # print(i,"_____",j)
            # не берет новости без заголовков
            if j[0]!="":
                final_dict[j[0]] = [j[1], j[2], day_time, i, j[4]]
            # final_dict[j[0]] = [j[1], j[2], j[3], i, j[4]]

        return final_dict



    # ==================================================
    def sorted_dicts(news_dict):
        """Сортировка словаря по дате элементов(новостей). Вверху самые поздние """
        sorted_dict = {}
        sorted_keys = sorted(news_dict, key=news_dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = news_dict[w]
        count_news = len(sorted_dict)
        # print('количество новостей = ', count_news)
        # print(sorted_dict)
        return sorted_dict

    ddd = filter(merge_dict(read_json(), dict_total))
    # print(ddd)
    dddd = sorted_dicts(ddd)
    # print(dddd)
    return dddd



# ========================================


def totaldate(date_dict):
    """Запись словаря с данными после парсера в GLdate0.json json-файл."""

    path1 = f"{path_bd_json}GLdate0.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(date_dict, file, ensure_ascii=False, indent=0)


# print("x", scrap_news())
# totaldate(scrap_news())

def write_base(diapason):  # int
    """диапазон  хранения данных за сколько дней"""

    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    dict_Nday_ago = {}

    # сделать словарь от начала дня 1дeн назад (вчера,) до Настоящего
    # времени

    # Определение  секунды сначала эпохи для начала текущего дня

    ddday = str(datetime.datetime.now())[:10]
    # print(ddday)
    today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
    # Определение  секунды сначала эпохи для начала  дня 3дня назад (вчера, позавчера, поза-позавчера)
    startNd_ago = today_start_ - 86400 * diapason
    startNd = today_start_ - 86400 * (diapason - 1)
    # print("start1d_ago", startNd_ago)
    # print('yesterday_start_', today_start_ - 86400)
    # исключение данных ранее даты start3d_ago
    for j, i in json_data_news.items():
        # print(j,"___",i)
        if startNd_ago <= i[0] <= startNd:
            # print(j, "___", i)
            dict_Nday_ago[j] = i

    path1 = f"{path_bd_json}GLdate{diapason}.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate{diapason}.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate{diapason}.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(dict_Nday_ago, file, ensure_ascii=False, indent=0)
    # print("3", dict_1day_ago)


def div_base():
    """сколько дней помним"""
    for diapason in range(1, 7):
        write_base(diapason)


def get_count_news():
    """создает список: количество новостей в каждой папке GLdate0.json-GLdate10.json"""
    number_news =[]
    for day_ago in range(11):
        path2 = f"{path_bd_json}GLdate{day_ago}.json"
        # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
        #         f"\\GLdate{day_ago}.json"
        # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate{day_ago}.json"

        with open(path2, 'r', encoding='utf-8') as f_five:
            json_data_news = json.load(f_five)

        count=len(json_data_news)

        number_news.append(count)
    qual_index=(number_news[7]+number_news[8]+number_news[9])/number_news[0]
    # print(f'Полнота отбора в рубрики: анонс, происшествия и общество___{qual_index}')
    path1 = f"{path_bd_json}numnews.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\numnews.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/numnews.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(number_news, file, ensure_ascii=False, indent=0)



# ========================================

def get_dates():
    """дает даты(день, месяц, год) дней -  вчера , позавчера, ..., 6 дней назад"""

    date_format = '%d.%m.%Y'
    day1 = datetime.datetime.now()
    list_days= []
    for i in range(1, 7):
        fd=day1 - datetime.timedelta(days=i)
        list_days.append(fd.strftime(date_format))

    return list_days


def script_scrap():
    totaldate(scrap_news())
    div_base()
    anons()
    accidents()
    societ()
    get_count_news()
    jkh()
    print("===============scrap============")


# script_scrap()




# подключение функции скрапинга вторым потоком, иначе не запускается сервер
def main():
    # script_scrap()

    t = threading.Thread(target=script_scrap)
    t.start()




main()

