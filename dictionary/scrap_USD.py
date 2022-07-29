import requests
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
    except:
        pass
# ====================================================


scrap_USD()