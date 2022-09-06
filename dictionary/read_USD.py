import json
import os
from dictionary.paths_01 import path_usd_json




def get_USD():
    """Выборка последнего json-файла для показа на сайте и конвертация в обычный словарь"""
    fild_bd = []
    #Перебор всех имен файлов в папке и запись в список имен
    for root, directory, file in os.walk(path_usd_json):
        # print(root)
        # print(directory)
        for file_bd in file:
            fild_bd.append(file_bd)
    # Выборка позднего json-файла для показа на сайте
    print(max(fild_bd))
    #конвертация в обычный словарь
    path2=f"{path_usd_json}{max(fild_bd)}"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)
    print(json_data_news)
    return json_data_news

