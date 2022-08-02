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

# data_dict={'02':[2,'1'],'03':[3,'2'],'04':[4,'1'],'05':[7,'2'],'06':[7,'1']}
# def read_json():
#     path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json\\GLdate.json"
#
#     with open(path2, 'r', encoding='utf-8') as f_five:
#         json_data_news = json.load(f_five)
#     print(json_data_news)
#     return json_data_news
#
# print(read_json())

# c:\Users\79081\Downloads\py\

# def totaldate(ddict):
#
#     """Запись словаря с данными после парсера в GLdate.json json-файл."""
#
#     path1 = f"C:\\Users\\79081\\Downloads\\py\\GLdate.json"
#
#     with open(path1, 'w', encoding ='utf-8') as file:
#         json.dump(ddict, file, ensure_ascii=False, indent=0)
#
#
# totaldate(data_dict)


news_dict={
"«Металлоинвест» построил в Железногорске две новые спортплощадки": [
[
1659347940,
"12:59"
],
"12:59 01.08.2022",
"https://seyminfo.ru/metalloinvest-postroil-v-zheleznogorske-dve-novye-sportploshhadki.html",
"www.seyminfo.ru"
],
"В Курской области за неделю произошло 47 пожаров": [
[
1659347520,
"12:52"
],
"01 августа 2 12:52",
"https://kursk-izvestia.ru/news/187745/",
"www.kursk-izvestia.ru"
],
"В Курске за неделю составили 22 протокола из-за незаконной торговли": [
[
1659347460,
"12:51"
],
"12:51 01.08.2022",
"https://seyminfo.ru/v-kurske-za-nedelju-sostavili-22-protokola-iz-za-nezakonnoj-torgovli.html",
"www.seyminfo.ru"
],
"В Коренево Курской области женщину зажало между двумя автомобилями": [
[
1659347220,
"12:47"
],
"Сегодня, 12:47",
"https://46tv.ru/odnoj-strokoj/v-kurske/171726-v-korenevo-kurskoj-oblasti-zhenschinu-zazhalo-mezhdu-dvumja-avtomobiljami.html",
"www.46tv.ru"
]}
start3d_ago=1659347460
for j, i in news_dict.items():
    # print(j,"___",i)
    if start3d_ago <= i[0][0]:
        print(j, "___", i[0][0])
        # dict_3day_ago[j] = i
