
# def loggics(x):
#     ee=x.upper()
#     # ff=[]
#     ff={}
#     for i in range(5):
#         ee=ee+str(i)
#         # ff.append(ee)
#         ff[i]=[ee,i]
#     return ff
#
# if __name__ == '__main__':
#     print(loggics('fkf'))


import pickle
import re

# shoplistfile = 'shoplist1.data'


# def search_mod(shoplistfile,words):
#     # поиск в словарях
#     """
#     модуль для поиска текста по поисковому запросу(слову или выражению) и распечатка его из
#     файлов указанных параметре функции (в листе shoplistfile)
#     """

def search_words( words):
    # shoplistfile=f'dictionary\\all_hcob.data'
    # shoplistfile=f'static\\all_hcob.data'
    # shoplistfile=f'static\\PackScn0522.data'
    shoplistfile=f'c:\\Users\\79081\\PycharmProjects\\HoroscopeFolder\\PackScn0522.data'
    len_words=len(words )
    f = open(shoplistfile, 'rb')
    base = pickle.load(f)
    fragment=0
    nothing = 0
    words = words.lower()

    list0 = []
    dict0 = {}

    if (words[0] == "'" and words[-1] == "'") or (words[0] == '"' and words[-1] == '"'):
        words = words[1:-1]
        words = f' {words} '
        for name in base.keys():
            #     print(name,"x")
            if words in str(base[name][1]).lower():
                # print("=============================================================")
                print(name)
                print(base[name][0])

                # print(f"-------------------------------------------------------------{COLOR1}")
                ind = 0

                while words in str(base[name][1])[ind:].lower():
                    ind = base[name][1].lower().index(words, ind) + 1
                    if ind - 100 < 0:
                        start_ind = 0
                    else:
                        start_ind = ind - 100
                    result_text = [str(base[name][1])[start_ind:ind - 1],
                                  str(base[name][1])[ind - 1:ind + len_words - 3],
                                  str(base[name][1])[ind + len_words - 3:ind + 150]]
                    # pri1=(f'{result_text[0]}{result_text[1]}{result_text[2]}')
                    pri1 = [result_text[0], result_text[1], result_text[2]]
                    list0.append(pri1)
                    # print(f"___a", ind,r'//',len(base[name][1]), '____')
                    fragment += 1
                    # print()
                    # print()
                    # print()
                    dict0[name] = pri1
                nothing = + 1
                # dict0[name]=list0
    # =======================================================
    else:
        #     words_ls=words.split(' ')#.strip(',')
        #     print(words_ls[0],words_ls[1],words_ls[2])

        for name in base.keys():
            ind = 0
            # --------------------------------------
            words2 = []
            words_ls = words.split(' ')

            for ii in words_ls:
                ii = ii[:-1]
                ii = f"{ii}\.?"
                words2.append(ii)
            # print(key_)
            #         print(words2)
            key_ = '[а-я]?\s{0,2}\S{0,10}\s{0,2}\S{0,10}\s{0,2}'.join(words2)
            # key_=f"r'{key_}'"
            # print('key_=',key_)
            #         print(base[name][2][s:])
            # -----------------------------------

            result = re.findall(key_, str(base[name][1])[ind:].lower())

            #         print('result *=',result)
            if result:
                # print("===================================================================")
                # print()
                # print(name, "=")
                print('%%%',base[name][0])
                #             ind=0
                #             while re.findall(key_, base[name][2][ind:].lower()):
                for xx in result:

                    # print(
                    #     f"===================================================================")
                    ind = base[name][1].lower().index(xx, ind) + 1
                    if ind - 100 < 0:
                        start_ind = 0
                    else:
                        start_ind = ind - 100

                    result_text =[base[name][1][start_ind:ind-1],
                                  base[name][1][ind-1:ind+len_words-1],
                                  base[name][1][ind+len_words-1:ind + 150]]
                    # pri1=(f'{result_text[0]}{result_text[1]}{result_text[2]}')
                    pri1=[result_text[0],result_text[1],result_text[2]]
                    print('***************************************')
                    print(name)
                    print('***************************************')
                    print(pri1)
                    print('================================================')
                    pri2=(f"___b", ind,r'//',len(base[name][1]), '____')
                    fragment+=1
                    list0.append(pri1)
                    list0.append(f'====={name}========')
                    # print(shoplistfile)
                    # print()
                    # print()
                    dict0[name] = pri1

                nothing = + 1
                # dict0[name] = list0


    # if nothing == 0:
    #     # print("===================================================================")
    #     # print(f"{WW}                                                                   {WHITE}")
    #     # print(f"{WW}                                                                   {WHITE}")
    #     # print(f"{WW}                                                                   {WHITE}")
    #     # print("===================================================================")
    #     print(f"    Упс!Ничего не найдено! Попробуйте изменить запрос!           ")
    #
    #     # print(f"              по базе  ={shoplistfile}=")
    #     # print()
    # else:
    #     # print(f"                       ___{fragment} совпадений___")
    #     # print(f"{COLOR}             = Поиск по базе {shoplistfile} окончен = {WHITE}")
    #     # print("===================================================================")
    #     # print()

    return dict0,fragment
# words = input(f"{COLOR}        введите запрос:-->   {WHITE}")
    # return search_words

    # for catalog in shoplistfile:
    #     search_words(catalog, words)


# ============================================================

if __name__ == '__main__':

    # где ищется, по какой базе"
    # shoplistfile = 'shoplist2.data'
    # shoplistfile = 'all_hcob.data','all_hco_pl.data'
    # shoplistfile = 'all_hcob.data','all_hco_pl.data','vol1_hcob.data'
    # shoplistfile = 'hcob1.data'
    # shoplistfile = 'all_hco_pl.data'
    # shoplistfile = 'vol1_hcob.data'
    # search_words(shoplistfile, words)
    search_words(words)
    # search_words( input())
    # search_mod(shoplistfile,words)