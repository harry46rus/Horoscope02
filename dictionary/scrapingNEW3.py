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




def scrap(day_ago):
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""

    # #чтение и конвертация в обычный словарь
    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate{day_ago}.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\numnews.json"

    with open(path1, 'r', encoding='utf-8') as f_five:
        numnews = json.load(f_five)

    return json_data_news, numnews


# def scrap1():
#     """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""
#
#     # #чтение и конвертация в обычный словарь
#     path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate1.json"
#
#     with open(path2, 'r', encoding='utf-8') as f_five:
#         json_data_news = json.load(f_five)
#
#     return json_data_news
#
#
# def scrap2():
#     """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""
#
#     # #чтение и конвертация в обычный словарь
#     path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate2.json"
#
#     with open(path2, 'r', encoding='utf-8') as f_five:
#         json_data_news = json.load(f_five)
#
#     return json_data_news


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
        """конвертация даты публикации сайта-источника и приведение (конвертация) к стандртному
        виду"""
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

        return sec, hours_

    # ==================================================================

    def kurskcity():

        link = "https://kurskcity.ru/news/main"
        """дата в формате ( 16 июля 2022 года, 22:03)"""
        try:
            resp = requests.get(link, headers=header)
            print(resp.status_code, 'kurskcity.ru')
        except:
            print(resp.status_code, 'kurskcity.ru')
            # resp.raise_for_status()
        #     for i in range(58):
        #         try:
        news_dict = {}
        news_list = []

        soup = BeautifulSoup(resp.text, 'lxml')
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
                print(f"=====ошибка скрапинга кода kurskcity.ru=====итераций_{y}=========")
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
        news_dict = {}
        page_site = ['', '?page=1']
        for x in page_site:
            link = "https://gtrkkursk.ru/news-list" + x

            """дата в формате ( чт, 4 августа 2022 - 17:22)"""
            try:
                resp = requests.get(link, headers=header)
                print(resp.status_code, 'gtrkkursk.ru')
            except:
                print(resp.status_code, 'gtrkkursk.ru')
                # resp.raise_for_status()
            #     for i in range(58):
            #         try:

            news_list = []

            soup = BeautifulSoup(resp.text, 'lxml')
            for i in range(12):
                try:
                    News6 = soup.find('div', class_="view-content")#"сontent-wrap сontent-wrap-post")
                    News7 = News6.find_all('a',class_='item_pic-wrapper')[i].get('href')
                    reff = 'https://gtrkkursk.ru/' + News7

                    News8 = News6.find_all('h2',class_='title')[i].text#

                    News9 = News6.find_all('span',class_='item_time')[i].text#
                    time_iss = f'{News9[-23:-8]} {News9[-5:]}'
                    # time_iss = soup.find_all('div', class_="mainnewsdate small bltext")[i].text
                    news_dict[News8] = [convert(time_iss)[0], convert(time_iss)[1], time_iss, reff,
                      'www.gtrkkursk.ru']
                except:
                    print("===========ошибка скрапинга кода gtrkkursk.ru=========================")
                # print('News7'," ",News7)
                # print('News8'," ",News8)
                # print('News9'," ",News9)
                # print('time_iss'," ",time_iss)
                # print('reff'," ",reff)
            #     news_list = list(news_dict)
        return news_dict

    def s46tv():

        news_dict = {}
        link = "https://www.46tv.ru/odnoj-strokoj/v-kurske/"
        """дата в формате  (Сегодня, 18: 51) """
        try:
            resp = requests.get(link, headers=header)
            print(resp.status_code, '46tv.ru')
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
                news_dict[News41] = [convert(time_)[0], convert(time_)[1], time_, News42,
                                     'www.46tv.ru']
            except:
                print(f"=====ошибка скрапинга кода 46tv.ru=====итераций_{y}=========")
                break
        return news_dict

    #     # ======================================================
    def seyminfo():
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
                print(resp.status_code, 'seyminfo.ru')
            except:
                print(resp.status_code, 'seyminfo.ru')
            news_list = []

            soup = BeautifulSoup(resp.text, 'lxml')
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
                    print(f"=====ошибка скрапинга кода seyminfo.ru=====итераций_{y}=========")
                    break
        return news_dict

    # # ===============================================
    def k_izvestia():
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
                print(resp.status_code, 'kursk-izvestia.ru')
            except:
                print(resp.status_code, 'kursk-izvestia.ru')
            news_list = []

            soup = BeautifulSoup(resp.text, 'lxml')
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
                    print(f"=====ошибка скрапинга кода kursk-izvestia.ru=====итераций_{i}=========")
                    break
        return news_dict

    # # ==============================================
    def dddkursk():
        news_dict = {}
        link = "http://www.dddkursk.ru/lenta/"
        """дата в формате   (16 июля 2022, 17:12)"""
        try:
            resp = requests.get(link, headers=header)
            print(resp.status_code, 'dddkursk.ru')
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
                news_dict[News_5] = [convert(time_)[0], convert(time_)[1], time_, reff,
                                     'www.dddkursk.ru']

            except:
                print(f"=====ошибка скрапинга кода dddkursk.ru=====итераций_{y}=========")
                break
        return news_dict

    #     print("iterat_",iterat_)
    # =============================================
    dict_total = {}
    list_scr = [dict_total, kurskcity(), gtrkkursk(), s46tv(), seyminfo(), k_izvestia(), dddkursk()]
    for i in range(len(list_scr) - 1):
        # merge_dict(list_scr[0], list_scr[i+1])
        list_scr[0].update(list_scr[i + 1])
    print(list_scr[0])
    print(len(list_scr[0]))
    iterat_ += 1

    # =================================================

    def read_json():
        path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"

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
        print(ddday)
        today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
        # Определение  секунды сначала эпохи для начала  дня n-дня назад (вчера, позавчера,
        # поза-позавчера)
        start3d_ago = today_start_ - 86400 * 7
        print("start3d_ago", start3d_ago)
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
        """Сортировка словаря по дате элементов(новостей). Вверху самые поздние """
        sorted_dict = {}
        sorted_keys = sorted(news_dict, key=news_dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = news_dict[w]
        count_news = len(sorted_dict)
        print('количество новостей = ', count_news)
        # print(sorted_dict)
        return sorted_dict

    ddd = filter(merge_dict(read_json(), dict_total))
    # print(ddd)
    dddd = sorted_dicts(ddd)
    # print(dddd)
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
    """Запись словаря с данными после парсера в GLdate0.json json-файл."""

    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(date_dict, file, ensure_ascii=False, indent=0)


# print("x", scrap_news())
# totaldate(scrap_news())

def write_base(diapason):  # int

    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    dict_Nday_ago = {}

    # сделать словарь от начала дня 1дeн назад (вчера,) до Настоящего
    # времени

    # Определение  секунды сначала эпохи для начала текущего дня

    ddday = str(datetime.datetime.now())[:10]
    print(ddday)
    today_start_ = int(time.mktime(time.strptime(ddday, '%Y-%m-%d')))  # %H:%M')))
    # Определение  секунды сначала эпохи для начала  дня 3дня назад (вчера, позавчера, поза-позавчера)
    startNd_ago = today_start_ - 86400 * diapason
    startNd = today_start_ - 86400 * (diapason - 1)
    print("start1d_ago", startNd_ago)
    # print('yesterday_start_', today_start_ - 86400)
    # исключение данных ранее даты start3d_ago
    for j, i in json_data_news.items():
        # print(j,"___",i)
        if startNd_ago <= i[0] <= startNd:
            # print(j, "___", i)
            dict_Nday_ago[j] = i

    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate{diapason}.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(dict_Nday_ago, file, ensure_ascii=False, indent=0)
    # print("3", dict_1day_ago)


def div_base():
    """сколько дней помним"""
    for diapason in range(1, 7):
        write_base(diapason)


def get_count_news():
    """сколько файлов  7 по дням, анонсы , происшествия,..."""
    number_news =[]
    for day_ago in range(10):
        path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
                f"\\GLdate{day_ago}.json"

        with open(path2, 'r', encoding='utf-8') as f_five:
            json_data_news = json.load(f_five)

        count=len(json_data_news)

        number_news.append(count)
    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\numnews.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(number_news, file, ensure_ascii=False, indent=0)

# =====================================================
def anons():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""
    month_cirilic = {
        1: 'январ',
        2: 'феврал',
        3: 'март',
        4: 'апрел',
        5: 'мая',
        6: 'июн',
        7: 'июл',
        8: 'август',
        9: 'сентябр',
        10: 'октябр',
        11: 'ноябр',
        12: 'декабр'}

    anons_dict = {}

    def get_day_month(nn):

        """дает сегодняшнюю дату числом и месяц+nn(август+1=сентябрь"""
        сс = str(datetime.datetime.now())[:10]
        day_ = int(сс[8:])
        month0 = int(сс[5:7]) + nn
        if (int(сс[5:7]) + nn) > 12:
            month0 = month0 - 12
        month_ = month_cirilic[month0]
        return day_, month_

    # #чтение и конвертация в обычный словарь
    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():
        #
        key_list = [f'\d+ {get_day_month(1)[1]}', f'[пвнд][ао]? {get_day_month(1)[1]}',
                    f'\d+ {get_day_month(2)[1]}', f'[пвнд][ао]? {get_day_month(2)[1]}',
                    f'\d+ {get_day_month(3)[1]}', f'[пвнд][ао]? {get_day_month(3)[1]}',
                    f'\d+ {get_day_month(4)[1]}', f'[пвнд][ао]? {get_day_month(4)[1]}',
                    f'\d+ {get_day_month(5)[1]}', f'[пвнд][ао]? {get_day_month(5)[1]}',
                    f'[пвнд][ао]? \d+2[2,3,4] год']

        # август',
        for key_ in key_list:
            result = re.findall(key_, title.lower())
            # print(result)
            if result:
                # print(result)
                anons_dict[title] = y

    for title, y in json_data_news.items():
        key_ = f'\d+ {get_day_month(0)[1]}'
        result = re.findall(key_, title.lower())
        # print(result)
        # print(get_day_month(0)[0])
        if result:
            if int(result[0][:2]) > get_day_month(0)[0]:
                anons_dict[title] = y

    for title, y in json_data_news.items():
        # 'ся' учитывается и добавляется
        key_list1 = 'буд[еу]т|произойд[уе]т|установ[ия]т|начн[уе]т|создадут|представ[ия]т|\
                    наград[яи]т|анонс\w?|приглашают|провед[еу]т|восстановлен|восстанов[яи]т|\
                постро[яи]т|реконструиру[ею]т|установ[ия]т|заверш[аи]т|увелич[аи]т|уменьш[аи]т|\
                обеспеч[аи]т|огранич[аи]т|установ[яи]т|обяж[уе]т|провед[уе]т|познаком[яи]т|\
                законч[аи]т|презенту[юе]т|выдадут|потребу[ею]т|убер[уе]т|отключ[аи]т|посадят|\
                разработа[ю]т|застав[я]т|отпраздну[ю]т|назнач[и]т|постав[ия]т|запланиру[ею]т|\
                утверд[яи]т|выдел[яи]т|прекрат[ия]т|призов[еу]т|мобилизу[юе]т|выступ[ия]т|\
                перекро[юе]т|приглас[ия]т|отмет[ия]т|встрет[ия]т|распредел[ия]т|могут|станет|\
                благоустро[ия]т|появ[ия]тся|стро[ия]тся|постро[ия]т|приобрет[уе]т|провер[яи]т|\
                отправ[ия]т|пройд[еу]т|поддержат|реш[иа][лт]|ответит|подготов[ия]т|подбер[еу]т|\
                собира[ею]тся|обеспеч[аи]т|откро[ею]тся|замен[ия]т|заверш[аи]т|получ[аи]т|\
                ожида[ею]т|объяв[ия]т|оцен[ия]т|состо[ия]тся|стартовал|подтвердил|спилят|\
                отдохн[еу]т|демонтиру[юе]т |демонтировать|обеща[ею]т|упростил|открыл[ио]'

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        if result:
            res = re.findall(f'\d+ {get_day_month(0)[1]}', title.lower())
            if res:
                pass
            else:

                anons_dict[title] = y

    def sorted_dicts1(news_dict):
        """Сортировка словаря по дате элементов(новостей). Вверху самые поздние """
        sorted_dict = {}
        sorted_keys = sorted(news_dict, key=news_dict.get, reverse=True)  # [1, 3, 2]

        for w in sorted_keys:
            sorted_dict[w] = news_dict[w]
        count_news = len(sorted_dict)
        print('количество новостей = ', count_news)
        # print(sorted_dict)
        return sorted_dict

    sorted_anons_dict = sorted_dicts1(anons_dict)
    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate7.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_anons_dict, file, ensure_ascii=False, indent=0)
 # ==============================================


def accidents():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""


    accidents_dict = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    print(len(json_data_news))


    for title, y in json_data_news.items():

        # 'ся' учитывается и добавляется
        key_list1 = 'дтп\s|произош[е]?л\w?|случил[о]с?\w?|убийств\w?|подозрева\wт\w?|покушени\w?|\
                    обвиня\wтся|авари\w?|арест\w?|госпитализирован\w?|ранен\w?|осужд\w?\
                    похит\w? | п[р]?опал\w?| перелом\w?| изнасилов\w?|превышени\w \w? полномоч\w?|\
                    столкновени\w?|поврежд\w?|перевернул\w?| пострада\w?| жертв\w?|ищут|\
                    риговори\w?|тюрьм\w?|за решетку|сбил\w?|стрел\w?|горел\w?|пожар |убит|\
                    смерт\w\w |обманул\w?|мошенник\w|пресекли|обезвредили|поймал|выманил|\
                    оскорблени|угроз|аферист|госпитализирова|сжег|сожгла| краж|до смерти|\
                    пропал|пропав\w?|скончал\w?|убил\w?|задержал\w?|наркотик\w?|избил\w?|изиени\w?|\
                    махинац\w?|осквернил\w? труп\w?|спасател\w?|силовик\w?|служб\w?[- ]?112|\
                    беспилотн\w?|обнаружил\w?|по горячим следам|совращени\w?|лишил|утону|\
                    украл\w?|похитил\w?|террорист\w?|акт\w |незаконн\w?|обстрел\w?|диверси\w?|\
                    взрывоопасн\w? предмет\w?|нетрезв\w?|напал\w?|нападен\w?|артиллерийск\w?|\
                    снаряд\w?|выписал\w?|протокол\w?|несанкционирован\w?|торговл\w?|наркокурьер\w?|\
                    колони\w?|умер\w?|пострадал\w?|зареза\w?|миниров\w?|дебошир\w?|задержал\w?|\
                    пропал|поиски|диверсант| подорвал| подрывал'
        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        if result:
            accidents_dict[title] = y



    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate8.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(accidents_dict, file, ensure_ascii=False, indent=0)
        # =========================================


def societ():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""


    societ_dict = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 = ' построен| запущен| завершен\w?| преоборудован\w?| открыт\w?|\
                     остановлен\w?| прекращен\w?| обнародован\w?| планироан\w?|\
                     восстановле\w?| отремонтирован\w?| возобновлен\w?|станет|отметили|\
                     обновлен\w?| реконструирован\w?|административн\w?|будующ\w?|встретил\w?|\
                     курско\w? предприяти\w?| жил\w? застройк\w?| дорожн\w? развязк\w?|\
                     проходит|прокуратур\w?| добива[юе]тся|приглаша[ею]т| потратили|израсходован\w|\
                     потрачен\w|вложен\w| инвестированн\w| заплати\w?| вруч\w?|льгот|трудится|\
                     определ\w? порядок| палат\w| снизилась| повысилось| наград| нацпроект|\
                     школа|больниц| дум[аые]| бюджет| налоги| акцизы| платежи| голосование|\
                     в собственность регион|итоги работы|эскроу-счет|футбол|собственник|\
                     обеспечени\w безопасност|контракт|купили|приобрели| решил|предложил|\
                     нацпроект\w?|запуст\w?|ремонтирур\w?|открыти\w?|резервиров\w?|\
                     преми[еюяи]| уголовн| ипотек|спорт|авангард|причин[уаы]|обанкротил|\
                     добился|добились|комисси| готов[аы]?|упростил|проголосовал|%| подписал'

        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            societ_dict[title] = y



    path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
            f"\\GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(societ_dict, file, ensure_ascii=False, indent=0)

# =======================================================

time_list0 = ['00:00', '00:20', '00:40', '01:00',
              '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45',
              '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45',
              '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45',
              '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:37', '14:45',
              '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45',
              '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45',
              '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:51',
              '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45',
              '23:00', '23:20', '23:40'
              ]


def loop_serv(time_scrap):

    """запуск скрипта (парсера) по расписанию указанному в листе  'time_list0' """

    def sec_count(hour_min_):

        """вычисляет количесто секунд  от начала эпохи до сегодняшнего любого
         момента который дается  в формате  21:25 часы:минуты """
        full_date = f'{str(datetime.datetime.now())[:10]} {hour_min_}'
        secs_ = int(time.mktime(time.strptime(full_date, '%Y-%m-%d %H:%M')))
        return secs_

    while True:

        for hour_mins in time_scrap:
            print()
            print(f'Запуск в {hour_mins}')

            # print('secs',sec_count(hour_mins))

            ddday = str(datetime.datetime.now())[:16]
            print(ddday)
            sec0 = int(time.mktime(time.strptime(ddday, '%Y-%m-%d %H:%M')))
            # print('sec0', sec0)

            delta = sec_count(hour_mins) - sec0

            print(f'Ожидание {delta} секунд')
            # Если дата еще не наступила, то ждет ближайщую дату и запускает скрипт, потом дальще
            # повторяется все
            # print('not start==============')
            if delta > 0:
                sleep(delta)
                #
                print('start  of the NEWS-PARSER-script')

                totaldate(scrap_news())
                div_base()
                anons()
                accidents()
                societ()
                get_count_news()
            elif time_scrap[-1] == hour_mins:
                delta1 = 86400 - (sec_count(time_scrap[-1]) - sec_count(time_scrap[0]))
                print(f'ожидание {delta1} секунд до {time_scrap[0]}')
                print(time_scrap[-1], time_scrap[0])
                print(sec_count(time_scrap[-1]), sec_count(time_scrap[0]))
                sleep(delta1)
                totaldate(scrap_news())
                div_base()
                anons()
                accidents()
                societ()
                get_count_news()
# print(scrap())

# loop_serv()


# подключение функции скрапинга вторым потоком, иначе не запускается сервер
t = threading.Thread(target=loop_serv, args=(time_list0,))
t.start()




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
