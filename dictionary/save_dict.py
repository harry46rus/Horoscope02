import datetime
import json
import time

from paths_01 import path_bd_json


def rewrite_json():
    """записывает в архивную папку 'bd_json/arh_news/' месячный файл 'arh_news_08.22' из дневного
    файла новостей GLdate6 перед стиранием, поставить в Cron время выполнения этого
      скрипта не позднее 23:59. Вверху ранние(меньшие) даты внизу поздние(большие)"""

    path2 = f"{path_bd_json}GLdate6.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    # print(json_data_news)

    #определение месяца в новости
    time_values = [v[0] for v in json_data_news.values()]
    # print(time_values[0])
    # check_time = time.ctime(time_values[0])
    check_time = time.gmtime(time_values[0])
    cc = str(datetime.datetime.now())[:10]
    mounth=check_time.tm_mon
    year_=str(check_time.tm_year)[2:4]
    # print(check_time.tm_mon)
    # print(check_time,year_)

    path1 = f"{path_bd_json}arh_news\\arh_news_{mounth}{year_}.json"
    try:
        with open(path1, 'r', encoding='utf-8') as f_five:
            old_dict = json.load(f_five)
        # print(old_dict)
        # print(json_data_news)
        old_dict.update(json_data_news)

        with open(path1, 'w', encoding='utf-8') as file:
            json.dump(old_dict, file, ensure_ascii=False, indent=0)
    except:
        # old_dict={}
        with open(path1, 'w', encoding='utf-8') as file:
            json.dump(json_data_news, file, ensure_ascii=False, indent=0)
        # print(json_data_news)


rewrite_json()