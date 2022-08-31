import json
import re
import datetime
from dictionary.paths_01 import path_bd_json

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
        cc = str(datetime.datetime.now())[:10]
        day_ = int(cc[8:])
        month0 = int(cc[5:7]) + nn
        if (int(cc[5:7]) + nn) > 12:
            month0 = month0 - 12
        month_ = month_cirilic[month0]
        return day_, month_

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():
        #
        key_list = [f'\d+ {get_day_month(1)[1]}', f'[кпвнд][ао]? {get_day_month(1)[1]}',
                    f'\d+ {get_day_month(2)[1]}', f'[кпвнд][ао]? {get_day_month(2)[1]}',
                    f'\d+ {get_day_month(3)[1]}', f'[кпвнд][ао]? {get_day_month(3)[1]}',
                    f'\d+ {get_day_month(4)[1]}', f'[кпвнд][ао]? {get_day_month(4)[1]}',
                    f'\d+ {get_day_month(5)[1]}', f'[кпвнд][ао]? {get_day_month(5)[1]}',
                    f'[кпвнд][ао]? \d+2[2,3,4] год']

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
            if int(result[0][:2]) >= get_day_month(0)[0]: #только число (день)
                # print("gugu",result[0][:2],get_day_month(0)[0])
                anons_dict[title] = y

    for title, y in json_data_news.items():
        # 'ся' учитывается и добавляется
        key_list1 = 'буд[еу]т|произойд[уе]т|установ[ия]т|начн[уе]т|создадут|представ[ия]т\
               | наград[яи]т|анонс\w*|приглашают|провед[еу]т| н*[^е]* восстановлен|восстанов[яи]т\
               | постро[яи]т|реконструиру[ею]т|установ[ия]т|заверш[аи]т|увелич[аи]т|уменьш[аи]т\
               | обеспеч[аи]т|огранич[аи]т|установ[яи]т|обяж[уе]т|провед[уе]т|познаком[яи]т\
               | законч[аи]т|презенту[юе]т|выдадут|потребу[ею]т|убер[уе]т|отключ[аи]т|посадят\
               | разработа[ю]т|застав[я]т|отпраздну[ю]т|назнач[и]т|постав[ия]т|запланиру[ею]т\
               | утверд[яи]т|выдел[яи]т|прекрат[ия]т|призов[еу]т|мобилизу[юе]т|выступ[ия]т\
               | перекро[юе]т|приглас[ия]т|отмет[ия]т|встрет[ия]т|распредел[ия]т|могут|станет\
               | благоустро[ия]т|появ[ия]тся|стро[ия]тся|постро[ия]т|приобрет[уе]т|провер[яи]т\
               | отправ[ия]т|пройд[еу]т|поддержат|реш[иа][лт]|ответит|подготов[ия]т|подбер[еу]т\
               | собира[ею]тся|обеспеч[аи]т|откро[ею]тся|замен[ия]т|заверш[аи]т|получ[аи]т\
               | ожида[ею]т|объяв[ия]т|оцен[ия]т|состо[ия]т[ь]*ся|стартовал|подтвердил|спилят\
               | отдохн[еу]т|демонтиру[юе]т |демонтировать|обеща[ею]т|упростил|открыл[ио]\
               | объявил| готов|снесут| под снос|потратят|ожида[ею]т|начал\w* проверку\
               | строя| к зиме| к весне| к лету| к осени| получ[иа]т'

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
        # print('количество новостей = ', count_news)
        # print(sorted_dict)
        return sorted_dict

    sorted_anons_dict = sorted_dicts1(anons_dict)
    path1 = f"{path_bd_json}GLdate7.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate7.json"

    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate7.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_anons_dict, file, ensure_ascii=False, indent=0)
 # ==============================================


def accidents():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""


    accidents_dict = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        # 'ся' учитывается и добавляется
        key_list1 = ' дтп\s|произош[е]*л\w*|случил[о]с*\w*|убийств\w*|подозрева\wт\w*\
                   | подозревае| покушени\w*|суд взыскал| выгорел\
                   | обвиня\wтся|авари\w*|госпитализирован\w*|ранен\w*|осужд\w*\
                   | хищен\w* | п[р]*опал\w*| перелом\w*| изнасилов\w*|превышени\w \w* полномоч\w*\
                   | столкновени\w*|поврежд\w*|перевернул\w*| пострада\w*| жертв\w*|ищут\
                   | риговори\w*|тюрьм\w*|за решетку|сбил\w*|стрел\w*|горел\w*|пожар |убит\
                   | смерт\w\w |обманул\w*|мошенник|пресекли|обезвредили|поймал|выманил\
                   | оскорблени|угроз|аферист|госпитализирова|сжег|сожгла| краж|до смерти\
                   | пропал|пропав\w*|скончал\w*|убил\w*|наркотик\w*|избил\w*|изиени\w*\
                   | махинац\w*|осквернил\w* труп\w*|силовик\w*|служб\w*[- ]*112\
                   | беспилотн\w*|обнаружил\w*|по горячим следам|совращени\w*|лишил|утону\
                   | украл\w*|похитил\w*|террорист\w*|акт\w |незаконн\w*|обстрел\w*|диверси\w*\
                   | взрывоопасн\w* предмет\w*|нетрезв\w*|напал\w*|нападен\w*|артиллерийск\w*\
                   | снаряд\w*|выписал\w*|протокол\w*|несанкционирован\w*|торговл\w*\
                   | наркокурьер\w*|горит| вор\w|вор[уо]|клиент\w* банк|суд обязал\
                   | колони\w*|умер\w*|пострадал\w*|зареза\w*|миниров\w*|дебошир\w*|задержал\w*\
                   | пропал|поиски|диверсант| подорвал| подрывал| разбой| угонщик| просроченны\
                   | разбил| арест|отправ\w*т\w* в колонию|за нападение\
                   | попал в аварию| использовал\w* [\S*\s]* оружие| применил\w* [\S*\s]* оружие\
                   | угнан| укус\w* клещ'
        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        if result:
            accidents_dict[title] = y



    path1 = f"{path_bd_json}GLdate8.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate8.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate8.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(accidents_dict, file, ensure_ascii=False, indent=0)
        # =========================================


def societ():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""


    societ_dict = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 = ' построен| запущен| завершен\w*| преоборудован\w*| открыт\w*\
                    | остановлен\w*| прекращен\w*| обнародован\w*| планироан\w*\
                    | восстановле\w*| отремонтирован\w*| возобновлен\w*|станет|отметили\
                    | обновлен\w*| реконструирован\w*|административн\w*|будующ\w*|встретил\w*\
                    | курско\w* предприяти\w*| жил\w* застройк\w*| дорожн\w* развязк\w*\
                    | проходит|прокуратур\w*| добива[юе]тся|приглаша[ею]т|турнир\
                    | потратили|израсходован\w|строя| готов|обсуждают| фестиваль| оценил\
                    | потрачен\w|вложен\w| инвестированн\w| заплати\w*| вруч\w*|льгот|трудится\
                    | определ\w* порядок| палат\w*| снизилась| повысилось| наград| нацпроект\
                    | школа|больниц| дум[аые] | бюджет| налоги| акцизы| платежи| голосование\
                    | в собственность регион|итоги работы|эскроу-счет|футбол|собственник\
                    | обеспечени\w* безопасност|контракт|купили|приобрели| решил|предложил\
                    | нацпроект\w*|запуст\w*|ремонтирур\w*|открыти\w*|резервиров\w*\
                    | преми[еюяи]| уголовн| ипотек| спорт|авангард|причин[уаы]|обанкротил\
                    | добился|добились|комисси| готов[аы]*|упростил|проголосовал|%| подписал\
                    | победил| безработиц| инфляц| рост\w* цен| физкультур|запустил\
                    | археолог|индекс\w* потребительских цен|одержал\w [\S*\s]* победу\
                    | проходит| добил\w*с\
                    | контрол| получ[иа]т'

        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            societ_dict[title] = y



    path1 = f"{path_bd_json}GLdate9.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate9.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(societ_dict, file, ensure_ascii=False, indent=0)

# =======================================================