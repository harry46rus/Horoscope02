import json
import re
import datetime
import time

from paths_01 import path_bd_json

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
    anons_dict1 = {}
    anons_dict2 = {}

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

    ddd = f'{str(datetime.datetime.now())[:10]}'
    sec_now = int(time.mktime(time.strptime(ddd, '%Y-%m-%d')))

    for title, y in json_data_news.items():
        key_list = [f'\d\d.\d\d.\d\d+', ]

        # август',
        for key_ in key_list:
            result = re.findall(key_, title.lower())
            # print(result)
            if result:
                # print(result[0])
                xx = result[0]
                sec = int(time.mktime(time.strptime(xx, '%d.%m.%Y')))  # '04.07.2022'
                # day_ = datetime.datetime.now()
                # print(sec)
                # print(ddd)
                # print(sec_now)
                if sec_now <= sec:
                    anons_dict[title] = y
                    # print("@", y)


    # print(len(json_data_news))

    for title, y in json_data_news.items():
        #
        key_list = [f'\d+ {get_day_month(1)[1]}', f'[скпвнд][ао]? {get_day_month(1)[1]}',
                    f'\d+ {get_day_month(2)[1]}', f'[скпвнд][ао]? {get_day_month(2)[1]}',
                    f'\d+ {get_day_month(3)[1]}', f'[скпвнд][ао]? {get_day_month(3)[1]}',
                    f'\d+ {get_day_month(4)[1]}', f'[скпвнд][ао]? {get_day_month(4)[1]}',
                    f'\d+ {get_day_month(5)[1]}', f'[скпвнд][ао]? {get_day_month(5)[1]}',
                    f'[скпвнд][ао]? \d+2[2,3,4] год']

        # август',
        for key_ in key_list:
            result = re.findall(key_, title.lower())
            # print(result)
            if result:
                # print(result)
                anons_dict[title] = y

    # отсеивает более ранние даты чем сегодня
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
        key_list1 = r'буд[еу]т|произойд[уе]т|установ[ия]т|начн[уе]т|создадут|представ[ия]т|ььь\
          | наград[яи]т|анонс\w*|приглашают|провед[еу]т| н*[^е]* восстановлен|восстанов[яи]т|ььь\
          | постро[яи]т|реконструиру[ею]т|установ[ия]т|заверш[аи]т|увелич[аи]т|уменьш[аи]т|ььь\
          | обеспеч[аи]т|огранич[аи]т|установ[яи]т|обяж[уе]т|познаком[яи]т|слёт|хотят|ььь\
          | законч[аи]т|презенту[юе]т|выдадут|потребу[ею]т|убер[уе]т|отключ[аи]т|посадят|ььь\
          | разработа[ю]т|застав[я]т|отпраздну[ю]т|назнач[и]т|постав[ия]т|запланиру[ею]т|ььь\
          | утверд[яи]т|выдел[яи]т|прекрат[ия]т|призов[еу]т|мобилизу[юе]т|выступ[ия]т|ььь\
          | перекро[юе]т|приглас[ия]т|отмет[ия]т|встрет[ия]т|распредел[ия]т|могут|станет|ььь\
          | благоустро[ия]т|появ[ия]тся|стро[ия]тся|постро[ия]т|приобрет[уе]т|провер[яи]т|ььь\
          | отправ[ия]т|пройд[еу]т|поддержат|реш[иа][лт]|ответит|подготов[ия]т|подбер[еу]т|ььь\
          | собира[ею]тся|обеспеч[аи]т|откро[ею]тся|замен[ия]т|заверш[аи]т|получ[аи]т|ььь\
          | ожида[ею]т|объяв[ия]т|оцен[ия]т|состо[ия]т[ь]*ся|стартовал|подтвердил|спилят|ььь\
          | отдохн[еу]т|демонтиру[юе]т |демонтировать|обеща[ею]т|упростил|открыл[ио]|ььь\
          | объявил| готов|снесут| под снос|потратят|ожида[ею]т|начал\w* проверку|ььь\
          |строя| получ[иа]т|\bможно|сегодня|проходит|провод[ия]т|бесплатно окаж[еу]т|ььь\
          |прос[яи]т сообщ[аи]ть|прогноз чс|на контроле гу мчс|планиру[ею]т|\w*[яи]тся|ььь\
          |новогодн\w* ноч|(\bдо\b|\bк\b)[\s\w]{,20}(зим[ые]|весн[ые]|лет[ау]|осени)|запрещен'

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        if result:
            res = re.findall(f'\d+ {get_day_month(0)[1]}', title.lower())
            if res:
                pass
            else:
                anons_dict[title] = y
    #отсеивает со словом сегодня если дата раньше чем текущая
    for title, y in anons_dict.items():
        # работа со словом "сегодня"
        result = re.findall("сегодня", title.lower())
        if result:
            # print('сегодня_news')
            today_start_ = int(time.mktime(time.strptime(str(datetime.datetime.now())[:10],
                  '%Y-%m-%d')))
            delta = y[0] - today_start_
            # print(delta)
            if 0 < delta < 86400:
                anons_dict1[title] = y
                # print('сегодня_ ', title, y[2])
        else:
            anons_dict1[title] = y

    # исключение из словаря предложений с таким словами
    for title, y in anons_dict1.items():
        key_list2 = r'\bкраж|судит|нарушени|задержа|лишит\w* прав|украден|произош[е]л|случил|ььь\
                    |выявил|утонул|сгорел'

        result1 = re.findall(key_list2, title.lower())
        # print(result)
        if result1:
            pass
        else:
            anons_dict2[title] = y

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

    sorted_anons_dict = sorted_dicts1(anons_dict2)
    path1 = f"{path_bd_json}GLdate7.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate7.json"

    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate7.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_anons_dict, file, ensure_ascii=False, indent=0)
# ===============================
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
        key_list1 = r' дтп|произош[е]*л\w*|случил[о]с*\w*|убийств\w*|подозрева\wт\w*|ььь\
                   |подозревае| покушени\w*|суд взыскал| выгорел|уличил|ььь\
                   |обвиня\wтся|авари\w*|госпитализирован\w*|ранен\w*|осужд\w*|ььь\
                   |хищен\w*| п[р]*опал\w*| перелом\w*| изнасилов\w*|ььь\
                   |превышени\w[\s\w]{,20}полномоч\w*|таранил|пропал\w? без вести|ььь\
                   |столкновени\w*|поврежд\w*|перевернул\w*| пострада\w*| жертв\w*|ищут|ььь\
                   |риговори\w*|тюрьм\w*|за решетку|сбил\w*|стрел\w*|горел\w*|пожар |убит|ььь\
                   |смерт\w\w |обманул\w*|мошенни[кч]|пресекли|обезвредили|поймал|выманил|ььь\
                   |оскорблени|угроз|аферист|госпитализирова|сжег|сожгла| краж|до смерти|ььь\
                   |пропал|пропав\w*|скончал\w*|убил\w*|наркотик\w*|избил\w*|изиени\w*|ььь\
                   |махинац\w*|осквернил\w*|\bтруп\w*|силовик\w*|служб\w*[- ]*112|ььь\
                   |беспилотн\w*|обнаружил\w*|по горячим следам|совращени\w*|лишил|утону|ььь\
                   |украл\w*|похитил\w*|террорист\w*|акт\w |незаконн\w*|обстрел\w*|диверси\w*|ььь\
                   |взрывоопасн\w* предмет\w*|нетрезв\w*|напал\w*|нападен\w*|артиллерийск\w*|ььь\
                   |снаряд\w*|выписал\w*|протокол\w*|несанкционирован\w*|торговл\w*|ььь\
                   |наркокурьер\w*|горит|\bвор[аеуо]|клиент\w* банк|суд обязал|оштрафова[нл]|ььь\
                   |колони\w*|умер\w*|пострадал\w*|зареза\w*|миниров\w*|дебошир\w*|задержал\w*|ььь\
                   |пропал|поиски|диверсант| подорвал| подрывал| разбой| угонщик| просроченны|ььь\
                   |разбил| арест|отправ\w*т\w* в колонию|за нападение|фальшив|подделк|ььь\
                   |попал в аварию| использовал\w* [\S*\s]* оружие| применил\w* [\S*\s]* оружие|ььь\
                   |угнан| укус\w* клещ|\bподлог|\bфиктивн|(чужой|не своей)[\s\w]{,20}(картой)|ььь\
                   |\bподлог|\bзадержа|\bподделал|разыскива|полици|ранени|\bскончал|тушил|погиб|ььь\
                   |возгорани|гибел|покушени|изнасилова|план\w* \W?перехват|обокрал|преступлени|ььь\
                   |прос[я]т сообщ[и]т|потушил|врезал[и]?с|завал[и]?[л]?|правонарушени|ььь\
                   |дорожн\w* ситуац|сводк\w* чс|разлив\w* фекали|происшестви|лишени\w* свобод|ььь\
                   |распити[\s\w]{,30}в общественном месте|нецензурн\w* бран|насмерть замерз|ььь\
                   |провалил\w* под лёд|замерз\w* насмерть|опрокинул[с]?|тел[ао] мужчин|ььь\
                   |тел[ао] женщин|проститутк|притон'
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
# ===============================
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

        key_list1 = r' построен| запущен| завершен\w*| преоборудован\w*| открыт\w*|ььь\
                    | остановлен\w*| прекращен\w*| обнародован\w*| планироан\w*|субботник|ььь\
                    | восстановле\w*| отремонтирован\w*| возобновлен\w*|станет|отметили|ььь\
                    | обновлен\w*| реконструирован\w*|административн\w*|будующ\w*|встретил\w*|ььь\
                    | курско\w* предприяти\w*| жил\w* застройк\w*| дорожн\w* развязк\w*|ььь\
                    | проходит|прокуратур\w*| добива[юе]тся|приглаша[ею]т|турнир|рекорд|ььь\
                    | потратили|израсходован\w|строя| готов|обсуждают| фестиваль| оценил|ььь\
                    | потрачен\w|вложен\w| инвестированн\w| заплати\w*| вруч\w*|льгот|трудится|ььь\
                    | определ\w* порядок| палат\w*| снизилась| повысилось| наград| нацпроект|ььь\
                    | школа|больниц| дум[аые] | бюджет| налоги| акцизы| платежи| голосование|ььь\
                    | в собственность регион|итоги работы|эскроу-счет|футбол[оауе]|собственник|ььь\
                    | обеспечени\w* безопасност|контракт|купили|приобрели| решил|предложил|ььь\
                    | нацпроект\w*|запуст\w*|ремонтирур\w*|открыти\w*|резервиров\w*|ььь\
                    | преми[еюяи]| уголовн| ипотек| спорт|авангард|причин[уаы]|обанкротил|ььь\
                    | добился|добились|комисси| готов[аы]*|упростил|проголосовал|%| подписал|ььь\
                    | победил| безработиц| инфляц| рост\w* цен| физкультур|запустил|депутат|ььь\
                    | археолог|индекс\w* потребительских цен|одержал\w [\S*\s]* победу|ььь\
                    | добил\w*с|муниципал| слушани|совещан|мэр[иаоеу]|гимн|карт\w* жителя|ььь\
                    |семейнсемь[яиею]| контрол| получ[иа]т|госуслуг|\bit\Wтехнологи|ььь\
                    |обществен\w* транспорт|отметил|центр\w* занятости|старовойт|куцак|ььь\
                    |почтил\w* память|д[е]?н[юяь] неизвестного солдата|лунно\w* гало'


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
# ===============================
def jkh():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""


    jkh_dict = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 = r'жкх|без газа|гасоснабж|канализац|отключен|отключат|ььь\
                    |остановлен\w*|аварийны\w* дом|рассел[еия][тн]|ььь\
                    |восстановле\w*| отремонтирован\w*| возобновлен\w*|ььь\
                    |обновлен\w*|реконструирован\w*|жители дома|\bкотель[ны]|ььь\
                    |(отключени\w*|без|\bс\b)[\s\w]{,20}(вод[^и]|свет|электр|движени\w*)|ььь\
                    |дорожн\w* развязк\w*|капремонт|капитальн\w* ремонт|ььь\
                    |(вод|свет|электр)[\s\w]{,15}(отключени\w*)|«квадр[аыо]\w*»|ььь\
                    |(холодн|горяч)[\s\w]{,15}(вод)| мусор| свалк|\sтбо|ььь\
                    |подач\w газ\w| инвестированн\w|освещенн\w? улиц|теплосет\w*|ььь\
                    |(вод|свет|электр)[\s\w]{,15}(обещают)| дорожн\w* работ| нацпроект|ььь\
                    |(ремонт|укладк|строит|убирал|уборк)[\s\w]{,15}(доро[гж])|утилизаци\w* тко|ььь\
                    |(коммунальн\w*) (удобств|услуг)|\bотоплени|восстанов\w* освещение|ььь\
                    |водоснабжен'

        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            jkh_dict[title] = y



    path1 = f"{path_bd_json}GLdate10.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate9.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(jkh_dict, file, ensure_ascii=False, indent=0)
# ===============================
def sport():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""


    sport_dict = {}
    sport_dict1 = {}



    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 =r'чемпионат|авангард|бокс|маунтинбайк|\bспорт|рекорд по|ььь\
                |турнир|гимнаст|физкультур|рапирист|динамо|биатлон|ььь\
                |пауэрлифт|ипподром|спартакиад|регби|евролиг|лыжн[оиы]|ььь\
                |стритбол|забег|болельщик|кикбоксинг|тренировочн\w* сбор|ььь\
                |дзюдо|спортивн\w* борьб|паралимпий|троебор»|фитнес-центр|ььь\
                |марафон|плей-офф|единоборств|первенств|киокусинкай|волейбол|ььь\
                |куб[о]?к\w* России|спортивны\w* соревновани|спортивн\w* ориентирован|ььь\
                |легко\w* атлетик|шахмат|спартакиада|фехтовани|мастер\w* спорт|ььь\
                |многоборь|(завоевал)[\s\w]{,15}(золото|серебр|бронз)|олимпиад|ььь\
                |олимпийск\w* д[е]?н[я]?|автокросс| мотокросс|бегун|пауэрлифтинг|ььь\
                |кросс|карат[еи]|плавани|скейтбординг|баскетбол|чемпионск\w* титул|ььь\
                |футбол|акробатическ\w* рок-н-ролл|(велосипедн\w*) (гонк|спорт)|ььь\
                |парашут\w* спорт|кат[о]?к[е]? с искусственным льдом|бодибилдинг|ььь\
                |спортивн\w* стрельб|триатлон|соревновани\w* по|болельщик'


        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            sport_dict[title] = y
        # исключение из словаря предложений с таким словами
    for title, y in sport_dict.items():
        key_list2 = r'\bполиц|«соль»'

        result1 = re.findall(key_list2, title.lower())
        # print(result)
        if result1:
            pass
        else:
            sport_dict1[title] = y


    path1 = f"{path_bd_json}GLdate11.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sport_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def medicin():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""

    medicin_dict = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"
    # path2 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate0.json"
    # path2 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 =r'поликлиник|больниц|амбулатори|скор\w* помощ|ььь\
                |covid|ковид|вакцин|коронавирус|омикрон|санитарн|медкарт|ььь\
                |санавиаци|масочн\w* режим|карт\w* пациент|пациент|больничны|ььь\
                |«спутник\w* v»|«ковиваком»| привив|«эпиваккорон\w*»|онколог|ььь\
                |медицин|смертност|стоматолог|лечени|анестези|инфаркт|ььь\
                |\bомс\b|медсестр|здравоохранени|\bрод[ыо]|пандеми|\bспид\b|ььь\
                |продолжительность жизни|перинатальн\w* центр|перинатальн|ььь\
                |инфекционн|бактери|медучрежден|донор\w* крови|онкоцентр|ььь\
                |уролог|(делал|выполнил|провел)[\s\w]{,15}(операц)|врач|ььь\
                |заболеван|грипп|заболел|здоровь|медик|иммунитет|ььь\
                |\bорви |планов\w* помощ|госпитал|\bклиник|\bвич[-]?\b'


        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            medicin_dict[title] = y



    path1 = f"{path_bd_json}GLdate12.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate9.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(medicin_dict, file, ensure_ascii=False, indent=0)
# ===============================
def education():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""

    education_dict = {}
    education_dict1 = {}
    education_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 =r'педагог|школ|детск\w* сад|детсад|академи|ььь\
                |абитуриент|\bегэ|выпускник|информатик|\bогэ\b|хакатон|ььь\
                |государственн\w* итогов\w* аттестац|\bвуз|учащиеся|ььь\
                | переобучени|\bурок|выпускни[кц]|\bюзгу|\bкгу|\bсха|ььь\
                |образовани|наставник|диктант|учител|\bуч[иа]т|\bизуч[иа]т|ььь\
                |научат|университет|колледж|воспитател|школьни[кц]|учени[кц]|ььь\
                |студент|грант|просвещени| дошколят|\bлице[йеюя]|ььь\
                |старшеклассни[кц]|учёны[йм]|олимпиад\w*[\s\w]{,12}по|гимназия|педсовет|ььь\
                |грамот|академи|стипендиат|грамотност|\bit|ььь\
                |последн\w* звон[o]к|выпускно\w|учебн\w* год'


        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            education_dict[title] = y

        # исключение из словаря предложений с таким словами
        for title, y in education_dict.items():
            key_list2 = r'на школьн|ул[.\w]* школьн'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # education_dict2[title] = y
                pass
            else:
                education_dict1[title] = y

    path1 = f"{path_bd_json}GLdate13.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate9.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(education_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def economic():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
    сайте) и  конвертация в обычный словарь"""

    economic_dict = {}
    economic_dict1 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 =r'выплат|предприяти|\bдолг[и]? |кредит|субсиди|ипоте[кч]|ььь\
                |экономик|\bналог|зарплат|информатик|льгот|\bсборы|медкарт|ььь\
                |производств|технологи|электронн|предпринимател|введен\w* в эксплуатацию|ььь\
                |сельхозтоваропроизводител|бюджет|деньг|\bбанк|отрасл|ььь\
                |финанс|социальн\w* сфер|(получ[иа]т|выплат)[\s\w]{,15}(рублей)|ььь\
                |кредитн\w* карт|экспорт|микрозайм|экономическ|инвестиц|ььь\
                |доход|платеж|систем\w* быстрых платежей|ввели в эксплуатацию|ььь\
                |богаты|бедны|сервис|цифров|эскроу|недвижимост|самозанят|ььь\
                |\bсчет|маткапитал|прожиточн\w* минимум|вве[лд][\s\w]{,25}\bжиль[яе]|ььь\
                |материнск\w* капитал|подорожал\w|подешевел\w* год|центр\w* занятости|ььь\
                |(начисл|банковск|кредитн|дебетов|пластиков)[\s\w]{,25}(карт)|ььь\
                |правительств|пенси[ийю]|бизнес|заемщик|средств|адресн\w* помощ|ььь\
                |индекс|банкрот|аграри|аренд|посевн|фермер|\bцен |\bцены|ььь\
                |платёжн\w* систем|потребител|экспорт|валют|нацпроект|росреестр|ььь\
                |(млн|млрд) (рублей)|акциз|обесцен|инфляци|урожай|закупк|ььь\
                |аграрны|норматив|доллар|убыт[о]?к|сев\w* озимых|гектар|ььь\
                |товаропроизводител|производител|федеральн\w* средств|роспотребнадзор|ььь\
                |ярмарк|задолжал|компенсац|\bминист[е]?|торговл|зерновы|подорожают'


        # 'ся' учитывается и добавляется

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            economic_dict[title] = y
    #исключение из словаря предложений с таким словами
    for title, y in economic_dict.items():
        key_list2 = r'мошенник|похити[лтв]|укра[вл]|лиши[вл]|потеря[вл]|отня[втл]|обману[тлв]|ььь\
                    |выманива|погиб| краж|подозреваемы|голосова[нв]|фиктивн|умер|ььь\
                    |отсудил|смерт|(чужой|не своей)[\s\w]{,20}(картой)|напал|ущерб|ььь\
                    |\bподлог|\bзадержа|\bподделал|в суде|судебн\w* иск|незаконно|ььь\
                    |призывн[ио]|сигарет|уличил|поздрав[ия]|скрыл|со счет|\bучил[иса]'

        result1 = re.findall(key_list2, title.lower())
        # print(result)
        if result1:
            pass
        else:
            economic_dict1[title] = y

    path1 = f"{path_bd_json}GLdate14.json"
    # path1 = f"C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\dictionary\\bd_json" \
    #         f"\\GLdate9.json"
    # path1 = f"/home/sovabot0/domains/sovabot.ru/horoscope/dictionary/bd_json/GLdate9.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(economic_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def culture():
    """Сортирует словарь событий по теме,  записывает json-файла по пути (для показа на
        сайте) и  конвертация в обычный словарь"""

    culture_dict = {}
    culture_dict1 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 = r'конкурс|фестивал|концерт|джаз|мастер-класс|мюзикл|ььь\
                    |экскурси|\bкино|\bактер|пев[ие]ц|\bпоэт|лектори|ььь\
                    |композитор|культур[еауо]|праздни[кч]|\bпоказ|крестн\w* ход|ььь\
                    |фильм|лауреат|премьер[аоы]|спектакл|выставк|\bпати|ььь\
                    |им\.\sпушкин|винцкевич|party|библиотек|филармрони|ььь\
                    |режисер|по радио|культурн\w*[-\s\w]{,10}мероприят|галере\w* «ая»|ььь\
                    |оркестр|солист|вернисаж|мемориал|туристическ\w* маршрут|ььь\
                    |(создадут|установ[ия]т|постав[ия]т)[\s\w]{,15}(памятник|доск)|ььь\
                    |благотворительн фонд|капелл|вечер\w* памяти|\bпьес[ыаоу]|ььь\
                    |художни[кц]|хореографическ|искусств|стипендиат|живопис|ььь\
                    |театр|\bтенор|xxi век|литературн|анимаци|\bмузе[йяея]|музыкальн|ььь\
                    |мастер-класс|пленэр|пушкинск\w* карт|художествен|мастериц|ььь\
                    |торжественн\w* открыти|ден\w* город|(творческ\w*)(встреч|вечер)|ььь\
                    |нов[ы]\w* год|традиционн\w* ремес|водян\w* мельниц|комеди[яеи]|ььь\
                    |джазов\w* провинци|диктант|скульптор|натюрморт|\bтворчес[кт]|ььь\
                    |недел\w* ремесла|городск\w* елк|фольклорн'

        # |(курск\w*|курян\w*)[\s\w]{,15}(предложил|пригла[шс])\

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            culture_dict[title] = y

     # исключение из словаря предложений с таким словами
    for title, y in culture_dict.items():
        key_list2 = r'\bбоевых|\bкраж'

        result1 = re.findall(key_list2, title.lower())
        # print(result)
        if result1:
            pass
        else:
            culture_dict1[title] = y

    path1 = f"{path_bd_json}GLdate15.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(culture_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def dtp():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    dtp_dict = {}
    dtp_dict1 = {}
    dtp_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))


    for title, y in json_data_news.items():

        key_list1 = r' дтп|сбил\w*произош[е]*л\w*| столкновени|перевернул\w*|ььь\
                   |авари[ияюе]|сбил[аи]?|превернул[аси]|врезал[а]?с[ья]?|ььь\
                   |выезд[\s\w]{,15}на[\s\w]{,15}переезд|столкнул|таранил|опрокинул[с]?|ььь\
                    |насмерть задавил| задавил\w* насмерть'
        # 'ся' учитывается и добавляется врезался|врезалась

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            dtp_dict[title] = y
            if result:
                dtp_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in dtp_dict.items():
            key_list2 = r'\bракет|\bпво|энергоснабжен|нехватк|дефицит|депресси|теплотрасс|ььь\
                        |теплосет|\bлини\w* электо|\bводо[сп]|под кол[её]с'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # dtp_dict2[title] = y
                pass
            else:
                dtp_dict1[title] = y

    path1 = f"{path_bd_json}GLdate16.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(dtp_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def fire():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    fire_dict = {}
    fire_dict1 = {}
    fire_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 = r'пожар|возгорани|тушил|воспламен[еи]|[с]?горел|\bдым|очаг\w? возгорания|ььь\
                    |потушен|вспыхнул'
        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            fire_dict[title] = y
            if result:
                fire_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in fire_dict.items():
            key_list2 = r'учения|урок|\bобж\b'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                fire_dict2[title] = y
                pass
            else:
                fire_dict1[title] = y

    path1 = f"{path_bd_json}GLdate17.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(fire_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def moshen():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    moshen_dict = {}
    moshen_dict1 = {}
    moshen_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 = r'мошен[н]?и[кч]|аферист|обман|\bпод видом|незакон\w* завладел|\bлже\
                    |безопасн\w* счет|потерял\w* деньги|потерял\w*[\s\w]{,25}рубл'
        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            moshen_dict[title] = y
            if result:
                moshen_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in moshen_dict.items():
            key_list2 = r'учения'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # moshen_dict2[title] = y
                pass
            else:
                moshen_dict1[title] = y

    path1 = f"{path_bd_json}GLdate18.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(moshen_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def lifting():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    lifting_dict = {}
    lifting_dict1 = {}
    lifting_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 = r'краж[аиоу]?|обокрал|угнал|угон|похити[тл]|хищен|\bукравш|грабил|украл|ььь\
                    |воровств|\bвор[ауое]?|обворовал'
        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            lifting_dict[title] = y
            if result:
                lifting_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in lifting_dict.items():
            key_list2 = r'учения|урок|\bобж\b'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # lifting_dict2[title] = y
                pass
            else:
                lifting_dict1[title] = y

    path1 = f"{path_bd_json}GLdate19.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(lifting_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def syd():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    syd_dict = {}
    syd_dict1 = {}
    syd_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 =r'\bсуд[иеаоуы]|\bосуд[ия]|присуди|\bпристав|\bсуд\b|осужден|подсудим|ььь\
                   |конфисковал|ходатайств\w* прокурор|ограничил\w* свобод|отсудил'

        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            syd_dict[title] = y
            if result:
                syd_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in syd_dict.items():
            key_list2 = r'учения|урок|\bобж\b'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # syd_dict2[title] = y
                pass
            else:
                syd_dict1[title] = y

    path1 = f"{path_bd_json}GLdate20.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(syd_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def svo():
    """Выборка  json-файла для показа на сайте и конвертация в обычный словарь"""

    svo_dict = {}
    svo_dict1 = {}
    svo_dict2 = {}

    # #чтение и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate0.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        json_data_news = json.load(f_five)

    # print(len(json_data_news))

    for title, y in json_data_news.items():

        key_list1 = r'\bсво\b|обстрел|\bвсу\b|\bднр\b|\bлнр\b|\bмин[аыу]\b|\bминомет|\bминир|ььь\
        |(границ\w*)[\s\w]{,30}(белгородс|курской)|украин|диверс[иа]|диверси|\bz[а-я]*|ььь\
        |госизмен|шпион|террористическ\w* опасност|подозрительн\w* лиц|мобилизаци|ььь\
        |минобороны|контрактник|служб\w* по контракту|учебн\w* стрельб|\bмобилиз[оау]|ььь\
        |военн\w* комиссар|(фейк\w*|слух\w*)[\s\w]{,30}(эвакуац)|военком|призыв|ььь\
        |специальн\w* военн\w* операци|спецопераци|ополчен[ец]|систем\w* пво|чвк [«"]вагнер'
        # 'ся' учитывается и добавляется

        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        # print(result)
        if result:
            svo_dict[title] = y
            if result:
                svo_dict[title] = y
        # исключение из словаря предложений с таким словами
        for title, y in svo_dict.items():
            key_list2 = r'циклон|урок|\bобж\b'

            result1 = re.findall(key_list2, title.lower())
            # print(result)
            if result1:
                # svo_dict2[title] = y
                pass
            else:
                svo_dict1[title] = y

    path1 = f"{path_bd_json}GLdate21.json"
    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(svo_dict1, file, ensure_ascii=False, indent=0)
# ===============================
def today_(mm):
    """Выбирает события из json-файла и записывает в json-файл с датами события происходящими
       в этот день,mm=0 сегодня, mm=1 завтра, mm=2 послезавтра"""
    today_dict={}

    # #чтение anons и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate7.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        anons_dict = json.load(f_five)
 # ================================
    # со словом сегодня , дата совпадает с датой выпуска новости
    if mm == 0:
        for title, y in anons_dict.items():
            # работа со словом "сегодня"
            result = re.findall("сегодня", title.lower())
            if result:
                # print('сегодня_news')
                today_start_ = int(time.mktime(time.strptime(str(datetime.datetime.now())[:10],
                      '%Y-%m-%d')))
                delta = y[0] - today_start_
                # print(delta)
                if 0 < delta < 86400:
                    today_dict[title] = y
                    # print('сегодня_ ', title,' ; ',y[2])

        # print('zzz',today_dict)
# ================================================
    #
    month_cirilic = { 1: 'январ', 2: 'феврал', 3: 'март', 4: 'апрел', 5: 'мая', 6: 'июн',
        7: 'июл', 8: 'август', 9: 'сентябр', 10: 'октябр', 11: 'ноябр', 12: 'декабр'}

    def get_day_month(nn):

        """дает сегодняшнюю дату числом и месяц+nn(август+1=сентябрь)и месяц числом
        n=0 - текущий месяц, n=1 - следущий месяц"""
        cc = str(datetime.datetime.now())[:10]
        day_ = int(cc[8:])
        month0 = int(cc[5:7]) + nn
        if (int(cc[5:7]) + nn) > 12:
            month0 = month0 - 12
        month_ = month_cirilic[month0]
        return day_, month_,month0 #10,сентябр,9

# =================================================
    # добавляет только  с совпалдающей датой
    for title, y in anons_dict.items():
        # mm = 0# 0-сегодня,1- завтра, 2- послезавтра
        key_= f'\d+ {get_day_month(0)[1]}'
        result = re.findall(key_, title.lower())

        if result:
            # print("&&&&", result, get_day_month(0)[0] + mm)
            # print('**', result)
            # today_dict[title] = y
            if int(result[0][:2]) == int(get_day_month(0)[0]+mm):  # только число (день)
                # print("gugu", result[0][:2], get_day_month(0)[0])
                today_dict[title] = y
                # print(title)

    # print("xxxxx", today_dict)
    # print(len(today_dict))
# =====================================================

    def transft(dd,mon,yy):
        """перевод даты в секунды от начала эпохи"""
        sec = int(time.mktime((yy, mon, dd, 0, 1, 0, 0, 0, 0)))
        #2022, 9, 28, 12, 0, 0, 0, 0, 0

        return sec
# ===========================================================
    ddday = str(datetime.datetime.now())[:16]
    year_=time.strptime(ddday, '%Y-%m-%d %H:%M').tm_year

    sec_today = int(time.mktime(time.strptime(ddday,
        '%Y-%m-%d %H:%M')))+86400*mm
 # ========================================================
    for title, y in anons_dict.items():
        # добавляет с 00 сентября по/до 00 сентября
        key_1 = f'с \d?\d {get_day_month(0)[1]}\w* [пд]о \d?\d {get_day_month(0)[1]}'

        result = re.findall(key_1, title.lower())
        if result:
            # print("----",result,get_day_month(0)[1])
            key2 = r'(\d?\d)'
            result1 = re.findall(key2, result[0])
            start_time = transft(int(result1[0]),int(get_day_month(0)[2]),int(year_))
            # print(result1[0])
            finish_time = transft(int(result1[1]), int(get_day_month(0)[2]), int(year_))
            # print(result1[1])
            if start_time<=sec_today<=finish_time:
                today_dict[title] = y
                # print(title)

# ================================================================
        # добавляет с 00 -/по/до 00 сентября
        key_2 = f'с?\s?\d?\d\s?[-ипд]о?\s?\d?\d {get_day_month(0)[1]}'
        result = re.findall(key_2, title.lower())
        if result:
            # print("-==-", result, get_day_month(0)[1])
            key2 = r'(\d?\d)'
            result1 = re.findall(key2, result[0])
            # print(result1[0],get_day_month(0)[2],year_)
            start_time = transft(int(result1[0]), int(get_day_month(0)[2]), int(year_))
            # print(result1[0])
            finish_time = transft(int(result1[1]), int(get_day_month(0)[2]), int(year_))
            # print(result1[1])
            if start_time <= sec_today <= finish_time:
                today_dict[title] = y
                # print(title)
# ==================================================
        # добавляет с 00 сентября по/до 00 октября(в сентябре)
        key_1 = f'с \d?\d {get_day_month(0)[1]}\w* [пд]о \d?\d {get_day_month(1)[1]}'

        result = re.findall(key_1, title.lower())
        if result:
            # print("-=-=", result, get_day_month(0)[1])
            key2 = r'(\d?\d)'
            result1 = re.findall(key2, result[0])
            start_time = transft(int(result1[0]), int(get_day_month(0)[2]), int(year_))
            # print('*-*',result1[0])
            finish_time = transft(int(result1[1]), int(get_day_month(1)[2]), int(year_))
            # print('*-*',result1[1])
            if start_time <= sec_today <= finish_time:
                today_dict[title] = y
                # print('***',title)
# ==================================================
        # добавляет с 00 сентября по/до 00 октября(в октябре)
        key_1 = f'с \d?\d {get_day_month(-1)[1]}\w* [ипд]о? \d?\d {get_day_month(0)[1]}'

        result = re.findall(key_1, title.lower())
        if result:
            # print("-=-=", result, get_day_month(0)[1])
            key2 = r'(\d?\d)'
            result1 = re.findall(key2, result[0])
            start_time = transft(int(result1[0]), int(get_day_month(-1)[2]), int(year_))
            # print('*-*', result1[0])
            finish_time = transft(int(result1[1]), int(get_day_month(0)[2]), int(year_))
            # print('*-*', result1[1])
            if start_time <= sec_today <= finish_time:
                today_dict[title] = y
                # print('***', title)
 # ================================================
        # добавляет  00.00.2022
        key_1 = r'\d?\d\.\d\d\.\d{2,4}'
        result = re.findall(key_1, title.lower())
        if result:
            # print("-*-*", result, get_day_month(0)[1])
            key2 = r'(\d?\d)'
            result1 = re.findall(key2, result[0])
            if int(result1[0])==int(get_day_month(0)[0]+mm) and \
                int(result1[1])==int(get_day_month(0)[2]):
                today_dict[title] = y
                # print("^^^^",title)
                # print("^^^^",int(result1[0]),int(get_day_month(0)[0]+mm),"and",
                # int(result1[1]),int(get_day_month(0)[2]))

# ===============================================
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

    sorted_today_dict = sorted_dicts1(today_dict)
    path1 = f"{path_bd_json}GLdate2{2+mm}.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_today_dict, file, ensure_ascii=False, indent=0)
# ===============================
def events():
    """Выбирает события из json-файла и записывает в json-файл с датами события происходящими
       в этот день,mm=0 сегодня, mm=1 завтра, mm=2 послезавтра"""
    events_dict={}

    # #чтение anons и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate7.json"

    with open(path2, 'r', encoding='utf-8') as f_five:
        anons_dict = json.load(f_five)
 # ================================
    for title, y in anons_dict.items():
        # 'ся' учитывается и добавляется
        key_list1 = r'конкурс|фестивал|концерт|джаз|мастер-класс|проект|\bсесси|ььь\
                    |экскурси|\bкино|\bактер|пев[ие]ц|\bпоэт|лектори|мюзикл|ььь\
                    |композитор|культур[еауо]|праздни[кч]|\bпоказ|крестн\w* ход|ььь\
                    |фильм|лауреат|премьер[аоы]|спектакл|выставк|\bпати|\bакци[яиюе]|форум|ььь\
                    |им\.\sпушкин|винцкевич|party|библиотек|филармрони|слёт|ььь\
                    |режисер|по радио|культурн\w*[-\s\w]{,10}мероприят|галере\w* «ая»|ььь\
                    |оркестр|солист|вернисаж|мемориал|туристическ\w* маршрут|ььь\
                    |(создадут|установ[ия]т|постав[ия]т)[\s\w]{,15}(памятник|доск)|ььь\
                    |благотворительн фонд|капелл|вечер\w* памяти|\bпьес[ыаоу]|ььь\
                    |художни[кц]|хореографическ|искусств|стипендиат|живопис|ььь\
                    |театр|\bтенор|xxi век|литературн|анимаци|\bмузе[йяея]|музыкальн|ььь\
                    |мастер-класс|пленэр|пушкинск\w* карт|художествен|мастериц|ььь\
                    |торжественн\w* открыти|ден\w* город|(творческ\w*)(встреч|вечер)|ььь\
                    |нов[ы]\w* год|традиционн\w* ремес|водян\w* мельниц|комеди[яеи]|ььь\
                    |джазов\w* провинци|диктант|скульптор|натюрморт|\bтворчес[кт]|ььь\
                    |чемпионат|авангард|бокс|маунтинбайк|\bспорт|рекорд по|ььь\
                    |турнир|гимнаст|физкультур|рапирист|динамо|биатлон|ярмарк|ььь\
                    |пауэрлифт|ипподром|спартакиад|регби|евролиг|лыжн[оиы]|ььь\
                    |стритбол|забег|болельщик|кикбоксинг|тренировочн\w* сбор|ььь\
                    |дзюдо|спортивн\w* борьб|паралимпий|троебор»|фитнес-центр|ььь\
                    |марафон|плей-офф|единоборств|первенств|киокусинкай|волейбол|ььь\
                    |куб[о]?к\w* России|спортивны\w* соревновани|спортивн\w* ориентирован|ььь\
                    |легко\w* атлетик|шахмат|спартакиада|фехтовани|мастер\w* спорт|ььь\
                    |многоборь|(завоевал)[\s\w]{,15}(золото|серебр|бронз)|олимпиад|ььь\
                    |олимпийск\w* д[е]?н[я]?|автокросс| мотокросс|бегун|пауэрлифтинг|ььь\
                    |кросс|карат[еи]|плавани|скейтбординг|баскетбол|чемпионск\w* титул|ььь\
                    |футбол|акробатическ\w* рок-н-ролл|(велосипедн\w*) (гонк|спорт)|ььь\
                    |парашут\w* спорт|кат[о]?к[е]? с искусственным льдом|ььь\
                    |спортивн\w* стрельб|триатлон|соревновани\w* по|болельщик|ььь\
                    |недел\w* ремесла'
        # key_list1 = ['[а-я]+[аеиюя]т\s',]#'[а-я]+ят ','[а-я]+ют ','[а-я]+ат ']

        result = re.findall(key_list1, title.lower())
        if result:
            events_dict[title] = y
            # print(result)
# ===============================================
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

    sorted_events_dict = sorted_dicts1(events_dict)
    path1 = f"{path_bd_json}GLdate25.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_events_dict, file, ensure_ascii=False, indent=0)
# ===============================
def adverts():
    """Выбирает события из json-файла и записывает в json-файл с датами события происходящими
       в этот день,mm=0 сегодня, mm=1 завтра, mm=2 послезавтра. Запускать после events()"""
    adverts_dict={}

    # #чтение anons и конвертация в обычный словарь
    path2 = f"{path_bd_json}GLdate7.json"
    with open(path2, 'r', encoding='utf-8') as f_five:
        anons_dict = json.load(f_five)
 # ================================
    path3 = f"{path_bd_json}GLdate25.json"
    with open(path3, 'r', encoding='utf-8') as f_five:
        events_dict = json.load(f_five)

# ==================================
    def differ_dict(dic1, dic2):
        """вычитание словарей dic1-dic2=dic3,словарь3 получается из словаря1 без
        ключей словаря2"""

        dic3 = dic1.copy()
        for key2 in dic2.keys():
            # print(key2)
            for key1 in dic1.keys():
                if key1 == key2:
                    dic3.pop(key1)
        return dic3

    adverts_dict = differ_dict(anons_dict,events_dict)
# ===============================================
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

    sorted_dict = sorted_dicts1(adverts_dict)
    path1 = f"{path_bd_json}GLdate26.json"

    with open(path1, 'w', encoding='utf-8') as file:
        json.dump(sorted_dict, file, ensure_ascii=False, indent=0)
# ===============================
# anons()
# accidents()
# societ()
# jkh()
# sport()
# medicin()
# education()
# economic()
# culture()
# dtp()
# fire()
# moshen()
# lifting()
# syd()
# svo()