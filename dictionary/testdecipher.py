import textwrap

# rezultt=[68, 40, 60, 70, 62, 88, -18, -4, 46, 2]#I

# rezultt=[-28, -60, -40, 44, -18, 4, -40, -96, -80, -74]#Б
# rezultt=[-38, -22, -66, -6, 42, 39, -68, -62, -80, -14]#Р


# rezultt=[-75, -60, -58, 65, 20, 55, -60, -85, -90, -60]
rezultt=[70,68,38,76,97,61,20,-46,-50,-36]
# 70;68;38;76;97;61;20;-46;-50;-36 | Маник E
description_=f'test'

def test_decipher(rezultt,name_filePDF2,xx22,xx197):
    name_fileTXT = f'C:\\Users\\79081\\PycharmProjects\\pyWEB_0\\horoscope02\\static\\{name_filePDF2}.txt'
    rezult_list = []
    rez_list = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 'jj']
    zz_list=[]

    # check randomity grapf
    if -95 < rezultt[0] < -38 and -100 < rezultt[1] < -65 and -96 < rezultt[2] < -63 and  \
       -83 <rezultt[3]< 35 and 3 < rezultt[4] < 45 and 22 < rezultt[5] < 72\
        and -92 < rezultt[6] < -55 and -98 < rezultt[7] < -35 and -90 < rezultt[8] < 18 and\
        -72 < rezultt[9] < 22:
        print("Случайный график. Это происходит, когда человек отвечает на вопросы теста\n "
              "случайным образом, потому что он не понимает вопросов или по каким-либо  причинам\n"
              "не был внимателен. Этот график не поддается объяснению.")
    else:
        # plt.text(1.5, 64, "= r a n d o m   g r a p h =", size=48, \
        #          weight='extra bold', color='crimson')

        def zone_checker(x):
            if x>=70:
                z=1
            elif 20 <= x < 70:
                z=2
            elif -40 <= x < 20:
                z=3
            else:
                z=4
            return z

        for i in range(10):
            # zone_checker(rezultt[i])
            # print(zone_checker(rezultt[i]))
            zz_list.append(f'{rez_list[i]}{zone_checker(rezultt[i])}')

            # [Кроме того, характеристика D (Уверенность) показывает промежуток времени, в течение которого результаты теста будут действительными. Чем выше D, тем дольше этот период.]

        rez_dict={'aa1': "A-стабильность.У Вас твердый устойчивый характер. Вы способны концентрировать внимание на ваших делах предельно хорошо. Вы принимаете решение, хорошо его обдумав, и можете указать пути его выполнения. У Вас есть свое собственное мнение, которое не зависит от ваших эмоций или чего-либо еще. Вы можете быть очень лояльным.",
                   'aa2':"A-стабильность.У Вас достаточно стабильный характер. Вы можете с небольшими затруднениями концентрировать ваше внимание на текущих делах. Вы пытаетесь принимать решения, хорошо обдумав и хорошо оцениваете некоторые из них. Но Вы не всегда способны делать это, так как иногда Вы зависите от собственных эмоций и эмоций окружающих. Ваше мнение имеет тенденцию меняться.",
                   'aa3':"A-стабильность.У Вас нестабильный характер. Вам довольно трудно сконцентрировать внимание на текущем деле, так как ваше внимание рассеяно на множество других дел или зафиксировано на какой-то неизученной вещи. Ваши решения не реальны, а оценки довольно слабы. Вы легко подвергаетесь влиянию окружающих, поэтому ваше мнение изменчиво. Вы часто меняете ваши решения.",
                   'aa4':"A-стабильность.У Вас жутко нестабильный характер. У Вас плохая память, и Вы не можете сконцентрировать внимание на текущей задаче. Ваше внимание компульсивно перепрыгивает с одного на другое. Вы подвержены гипнозу, и поэтому ваши суждения, решения и мнения нереальны. Люди с трудом понимают Вас, поэтому Вы неуверены и очень импульсивны.",
                   'bb0':f"B-счастье и подавленность (МАНИК).Волнистая линия вокруг точки B "
                       f"показывает, что утверждение на карточке о вашем уровне счастья не всегда соответствует действительности. Ваш уровень счастья очень нестабилен - периоды всеобщего счастья и любви часто сменяются депрессией и удрученностью. B1 В общем Вы довольно счастливы и бодры. Ваш подход к жизни полон юмора. Вы принимаете все с энтузиазмом и интересом. Вы надеетесь на будущее и перешагиваете все ваши неудачи. Любые проблемы или эмоциональные трудности Вы считаете лишь временными неудобствами. Вы легко возвращаетесь к нормальному состоянию духа.",
                   'bb1':"B-счастье и подавленность.В общем Вы довольно счастливы и бодры. Ваш подход к жизни полон юмора. Вы принимаете все с энтузиазмом и интересом. Вы надеетесь на будущее и перешагиваете все ваши неудачи. Любые проблемы или эмоциональные трудности Вы считаете лишь временными неудобствами. Вы легко возвращаетесь к нормальному состоянию духа.",
                   'bb2':"B-счастье и подавленность.Вы довольно счастливы и бодры, но не всегда. проблемы и трудности в вашей жизни выбивают Вас из равновесия, и Вам не всегда легко вернуться в уравновешенное и счастливое состояние. Иногда Вы чувствуете, что ваше хорошее настроение зависит от других людей и обстоятельств, чаще чем Вы сами управляете вашей жизнью.",
                   'bb3':"B-счастье и подавленность.Вы несчастливы и подавлены. У Вас пессимистический взгляд на жизнь. У Вас слишком много проблем и трудностей, поэтому обычно Вы - упавший духом, и Вам всегда трудно. Обычно Вы вините других людей, ситуацию или обстоятельства, нежели настоящие причины, в вашем подавленном состоянии, поэтому вашим друзьям и семье трудно с Вами.",
                   'bb4':"B-счастье и подавленность.Вероятно, все так плохо, что этот пункт даже не рассматривается.",
                   'cc1':"C-спокойствие и нервозность.Вы достаточно спокойны и невозмутимы, психически Вы - уравновешенный человек. Вы владеете собой. Вам не трудно держать себя в руках, независимо от любых происшествий вокруг Вас. Вы обладаете ровным темпераментом, и это помогает Вам в общении с семьей и друзьями. У Вас хорошее терпение.",
                   'cc2':"C-спокойствие и нервозность.Вообще Вы спокойный человек, однако неприятности вокруг Вас иногда Вас раздражают. Чаще у Вас неровный темперамент. У Вас бывают периоды нервного состояния, но Вы способны овладеть собой. Вы склонны иногда быть нетерпеливым и даже невыносимым, что создает трудности для вашей семьи и друзей.",
                   'cc3':"C-спокойствие и нервозность.Вы нервный и чрезмерно возбудимый человек. Ваши расстройства и волнения досаждают окружающим Вас. Вам трудно расслабиться, быть довольным собой или просто хорошо отдохнуть. Ваша привычка нервничать, о которой Вы даже не подозреваете, проявляется в раздражении. Вы легко отвлекаетесь и Вам трудно себя контролировать.",
                   'cc4':"C-спокойствие и нервозность.Вы абсолютно нервный человек. У Вас нет настоящего контроля над собой даже при обычных обстоятельствах. Вы не можете расслабиться или успокоиться даже на короткий промежуток времени. Ваша привычка нервничать и постоянное состояние волнения сильно Вас раздражают. Вы очень нереальны и действуете бурно и даже истерично в ваших поступках. Почти все, что угодно обращает Вас в состояние растерянности.",
                   'dd1':"D-уверенность.Вы очень уверены и полагаетесь на стабильность того, что Вы знаете и понимаете в жизни. Вы хорошо знаете себя, ваши активные и пассивные стороны, что Вы можете и чего не можете, ваши цели и амбиции в жизни. Ваше реалистическое отношение к себе не дает Вам совершать больших ошибок.",
                   'dd2':"D-уверенность.Вы полагаетесь на свою реалистичность, испытывая при этом небольшие затруднения. Вы понимаете, что можете быть намного лучше. Вы не достаточно уверены в своих способностях, поэтому Вы иногда колеблетесь в вашем субъективном восприятии. У Вас есть некоторые проблемы с осознанием, чего Вы хотите добиться в жизни, но Вы не совершаете больших ошибок в выборе жизненного пути.",
                   'dd3':"D-уверенность.Вы абсолютно независимы [как-то смахивает все-таки на "'зависимы'"],По натуре Вы независимый человек. Вы недостаточно уверены в себе, что мешает Вам достигнуть поставленных в жизни целей. Из-за вашей неуверенности Вы не знаете, что Вам нужно, а что - нет. Это намного серьезней для Вас, чем то, что Вы не осознаете своих возможностей.",
                   'dd4':"D-уверенность.Вы абсолютно независимы [как-то смахивает все-таки на "'зависимы'"], и у Вас недостаток уверенности в себе. Вы абсолютно не уверены в своем прошлом, настоящем и будущем. Вы не знаете, во что Вы верите, что Вы знаете и что Вам нужно делать в жизни. У Вас нереалистичный подход к жизни, но это осложняется тем, что Вы действительно не знаете, чего Вы хотите. У Вас нет никаких гарантий по отношению к самому себе.",
                   'ee0':"E-активность (МАНИК).Волнистая линия вокруг точки E показывает, что утверждение на карточке о вашей активности не всегда соответствует действительности. Ваш уровень активности очень нестабилен - периоды активности часто сменяются пассивностью. Вы делаете не то, что Вам хочется.",
                   'ee1':"E-активность.Вы по натуре очень активный человек. Способны осознать, что Вам нужно, подумать и сделать это. Вы четко организовываете то, что делаете и получаете хорошие результаты без или с небольшими огрехами. Вы не бросите то, что важно и необходимо для Вас, у Вас есть энергия и упорство для завершения любого дела.",
                   'ee2':"E-активность.Вы активный человек, но не способны завершить все, что Вы могли бы или хотели бы сделать. У Вас есть небольшие трудности с началом работы, а когда Вы все-таки начнете, Вам трудно довести ее до конца. Иногда Вы беретесь за то, что не сможете сделать или у Вас возникают затруднения с выбором занятия.",
                   'ee3':"E-активность.Вы не активный человек. Вам трудно начинать дела, которые Вам необходимо или хотелось бы сделать. После того, как Вы наконец начали дело, Вам также трудно его продвигать и закончить. Вам трудно на работе, поэтому и по другим причинам, Вам трудно ее сохранить.",
                   'ee4':"E-активность.Вы совсем не активный человек. Вам практически невозможно заставить себя начать даже очень необходимое для Вас дело, Вам так же очень трудно продвигать дело к завершению Ваша семья и начальники считают Вам ленивым и трудно управляемым, плохо относящимся к работе и вообще работающим с трудом.",
                   'ff1':"F-способность.По натуре Вы способный и открытый человек. Вы довольно хорошо справляетесь с выполнением того, что поставили перед собой в жизни. Вы непосредственны и прямы в отношениях с людьми не только на работе и в профессиональном общении, но и с семьей и друзьями. Благодаря таким прямым и ясным отношениям Вы способны контролировать людей и справляться с любой жизненной ситуацией.",
                   'ff2':"F-способность.По натуре Вы способный и открытый человек, но вероятно, не до такой степени, до какой должны или хотели бы быть. Несмотря на ваши способности, Вам немного трудно управлять вашей жизнью и работой. Часть ваших трудностей состоит в том, что Вы не слишком способны управлять людьми и давать необходимые инструкции.",
                   'ff3':"F-способность.Вы сдержанный и покорный в отношениях с людьми, и поэтому Вы не приспособлены к жизни. Вы послушны и обходительны с другими, так как Вы боитесь, что они подумают, скажут или сделают по отношению к Вам. Эта боязнь других людей не позволяет Вам быть искренним и открытым в вашей семье, с друзьями на работе.",
                   'ff4':"F-способность.Вы очень плохого мнения о жизни, так как Вы слишком сдержанны и покорны. Вы определенно интроверт (обращены в себя), который боится столкнуться с управлением людьми или чем-либо еще. Вы также боитесь всего, что не полностью Вам понятно. Эта боязнь создает хаос и проблемы для Вам с вашим окружением.",
                   'gg1':"G-ответственность.По натуре Вы довольно ответственный человек. Вы чувствуете, что Вы имеете определенный контроль над своей жизнью. Вы способны взять на себя что-либо и быть уверенным в удаче или провале дела. Вы способны встретить любую ситуацию лицом к лицу и решить ее наилучшим образом, вместо того, чтобы считать, что это обязанности других, или думать, что это все равно ничего Вам не даст.",
                   'gg2':"G-ответственность.Вы не настолько ответственны, насколько должны быть. Между прочим, это причина того, что другие, в большей или меньшей степени, управляют вашей жизнью, будь то босс, друг или член семьи. Вы могли бы намного лучше контролировать свою жизнь, но предпочитаете не брать на себя слишком много ответственности, так как если у Вас что-то не получится, Вы будете чувствовать себя виноватым.",
                   'gg3':"G-ответственность.Вы безответственны в вашей жизни и на работе. Вы сваливаете всю вашу ответственность на других, будь то босс, друг или член семьи. Вы знаете, что у Вас нет контроля над вашей жизнью, над тем, что Вы делаете, над тем, кто Вы и чего Вы хотите добиться в жизни. Хотя Вы чувствуете, что другие могут контролировать ваше поведение, Вы действительно неспособны по-настоящему контролировать себя.",
                   'gg4':"G-ответственность.Вы полностью безответственны. Вы обвиняете других в том, что они управляют вашей жизнью, но на самом деле все ваши неудачи происходят тогда, когда Вы оставляете вашу ответственность на других.",
                   'hh1':"H-критичность, объективность.Вы человек с высокой и правильной оценкой. Вы можете получать удовольствие от общения с вашим окружением. Вы правильно принимаете жизнь и способны видеть и плохие, и хорошие стороны людей и жизни. У Вас действительно правильная оценка ситуаций, поэтому Вы проницательный человек.",
                   'hh2':"H-критичность, объективность.Вы склонны к критике, но так же не можете быть справедливы в оценке людей и событий. Вы воспринимаете небольшие недостатки в людях слишком сильно, это не позволяет Вам правильно оценивать все их хорошие стороны. Вы не так хороши, как могли бы или должны бы быть.",
                   'hh3':"H-критичность, объективность.Вы критичный человек. Другим людям трудно с Вами, потому что Вы экспрессивны и, хотя и не всегда, порицаете других людей. Так как Вы всегда видите только плохую сторону, Вы не замечаете много хорошего. В результате у Вас слабая способность правильно оценивать людей и обстоятельства.",
                   'hh4':"H-критичность, объективность.Вы очень критичный человек. Вы высмеиваете устно и умственно все, что Вас окружает, это делает Вас невозможным для других людей. Вы, возможно, рассматриваете себя, как конструктивного критика или реалиста, однако в основном Вы - злобный человек. Это потому, что Вы видите очень мало хорошего в людях и жизни.",
                   'ii1':"I-открытость, замкнутость.Вы очень симпатизирующий человек, причем Вы способны планировать свои действия в различных ситуациях и понимать случившееся или происходящее лучше других. Вы способны анализировать ваши действия при любых обстоятельствах.",
                   'ii2':"I-открытость, замкнутость.Вы симпатизирующий, но не настолько, насколько надо бы быть. Хотя Вы с легкостью ставите себя на место другого человека или представляете себя в любой ситуации, Вы не всегда делаете это, тем самым не полностью проявляя свои способности. Так же Вы недостаточно понимаете причины ваших неуместных или несвоевременных действий или слов.",
                   'ii3':"I-открытость, замкнутость.Вы неспособны быть симпатизирующим. Вы не можете поставить себя на место другого, поэтому не можете понять точку зрения других и войти в их положение. Это делает Вас подлым, недобрым по отношению к другим и доставляет Вам кучу неприятностей в общении. Недостаток понимания делает Вас бесчувственным и трудным для большинства людей.",
                   'ii4':"I-открытость, замкнутость.Вы довольно хладнокровны и бессердечны. Вы совсем не способны поставить себя на место другого человека и понять его, поэтому людям, имеющим с Вами дело, очень трудно. Вы придаете себе и вашему мнению слишком большую значимость.",
                   'jj1':"J-уровень общения.Вы очень общительный человек и получаете удовольствие, разговаривая с людьми. Вы хорошо совмещаете различные роли и легко ведете беседу с большинством людей. Вы можете быть расслаблены или нет, в разговоре, но это не мешает Вам излагать ваши идеи и мнения.",
                   'jj2':"J-уровень общения.Вы способны легко общаться с другими людьми,но недостаточно для достижения больших успехов в социальной и деловой сферах. Вы склонны к застенчивости им антипатии к уверенным в себе людям. Для повышения вашего социального и делового статуса Вы несомненно должны улучшить свои ораторские способности.",
                   'jj3':"J-уровень общения.Вы замкнутый человек. Вам нелегко общаться с окружающими, возможно поэтому Вы чувствуете робость или Вам не нравятся люди. Человек уступчивый как Вы, боится, что другие найдут что-нибудь, дискредитирующее Вас. Ваша неспособность свободно общаться будет мешать Вам приобретать друзей и прогрессировать в вашей работе.",
                   'jj4':"J-уровень общения.Вы очень замкнутый человек. Это может быть результатом того, что Вы вообще застенчивы или испытываете антипатию к людям, или все это вместе. то, что Вы не общаетесь с людьми, приводит к тому, что никто о Вас практически ничего не знает. Ваша неспособность свободно общаться - это очень большая помеха в вашей жизни.",
                }
    #     wwww=""
    #     for v in zz_list:
    #         wwww+=str('\n'+"   "+rez_dict[v]+'\n')
    #          # rez_list.append(rez_dict[v])
    #
    #     return wwww #rez_list
    # # print(zone_checker(-25))
    #
    # print(textwrap.fill(test_decipher(rezultt),80))
        #'ee0'
        # ['aa3', 'bb4', 'cc3', 'dd2', 'ee3', 'ff3', 'gg3', 'hh4', 'ii4', 'jj4']
        if xx22 == 1:
            zz_list[4]='ee0'
        if xx197 == 1:
            zz_list[1]='bb0'

        print(zz_list)
        wwww=""
        for v in zz_list:
           rezult_list.append(f"   {rez_dict[v]}")
# =======================================
        if rezultt[2]<0 and rezultt[7]<0:
            rezult_list.append(f"   C={rezultt[2]} и H={rezultt[7]} низкие: Проблемы в настоящем. Одитинг противопоказан.Ups & down.")
# =======================================
        if rezultt[3]<0 and rezultt[9]>20:
            rezult_list.append(f"   D={rezultt[3]} низкий, J={rezultt[9]} высокий:Несдержанный.Компульсивный(навязчивые идеи). Одитинг.")
# =======================================
        if rezultt[3] < 0 and rezultt[6] > 20:
            rezult_list.append(f"   D={rezultt[3]} низкий, G={rezultt[6]} высокий: Вынужденный экстраверт.")

# =======================================
        if rezultt[0] < -40 and rezultt[1] < -40 and rezultt[2] < -40 and rezultt[6] < -40 and\
            rezultt[7]< -40 and rezultt[8] < -40 and rezultt[9] < -40  and rezultt[3]>= 20 and\
            rezultt[4] >= 20 and rezultt[5] >= 20:

            rezult_list.append(f"   D={rezultt[3]}, E={rezultt[4]}, F={rezultt[5]} высокие, остаток графика очень низкий: Капризный, безответственный, замкнутый, с перевернутыми динамиками.Потенциально вредный.")
# =======================================
        if rezultt[3] < 0 and rezultt[6] < 0 and rezultt[7] < 0 and rezultt[8] < 0:
            rezult_list.append(f"   D={rezultt[3]}, G={rezultt[6]}, H={rezultt[7]} и I={rezultt[8]}"
                f" низкие: Отрицает существование.")
# =======================================

        if rezultt[4] < 0 and rezultt[5] < 0 and rezultt[9] < 0 :
            rezult_list.append(f"   E={rezultt[4]}, F={rezultt[5]} и J={rezultt[9]} низкие: "
            f"Личность, возможно, испытывает недостаток гормонов и должен посоветоваться с квалифицированным врачом.")
# =======================================

        if rezultt[0] > 20 and rezultt[1] > 20 and rezultt[2] > 20 and rezultt[3] > 20 and \
                rezultt[4] < -20 and rezultt[5] < -20 and rezultt[6] > 20 and rezultt[7] > 20 \
                and rezultt[8] > 20 and rezultt[9] > 20:
            rezult_list.append(f"   E={rezultt[4]}, F={rezultt[5]} низкие: Если остаток графика "
              f"приемлемый, то личность склонна к алкоголизму и наркомании или с трудом сдерживается.")
# =======================================

        if rezultt[4] > 20 and rezultt[6] < -20:
            rezult_list.append(f"   E={rezultt[4]} высокий, G={rezultt[6]} низкий : Недостаточно инициативен")
# =======================================

        if rezultt[5] > 20 and rezultt[6] < -20 and rezultt[7] < -20 :
            rezult_list.append(f"   F={rezultt[5]} высокий, G={rezultt[6]} и H={rezultt[7]} низкие:"
                               f" Тяжелый человек. С ним тяжело долго находиться.")
# ======================================
        if rezultt[8] > 20 and rezultt[9] > 20 and rezultt[1] > 20 and -40 < rezultt[5] < 20 :
            rezult_list.append(f"   Высокие I={rezultt[8]}, J={rezultt[9]} и B={rezultt[1]}, "
               f"низкий или средний F={rezultt[5]}: Приятный и милый.Легкий в общении.")
# ======================================
        if rezultt[8] > 20 and rezultt[9] < -20:
            rezult_list.append(f"   I={rezultt[8]} высокий, J={rezultt[9]} низкий: Благосклонность.")
# ======================================
        if rezultt[0] < -20  and rezultt[2] < -20 and rezultt[3] < -20 and \
                 rezultt[6] < -20 and rezultt[7] < -20 and rezultt[9] < -20:

            rezult_list.append(f"   Низкие A, C, D, G, H, J: Плохой работник.")
# ======================================
        if rezultt[6] > rezultt[0] and rezultt[6] > rezultt[1] and rezultt[6] > rezultt[2] and\
            rezultt[6] > rezultt[3] and rezultt[6] > rezultt[4] and rezultt[6] > rezultt[5] and\
            rezultt[6] > rezultt[7] and rezultt[6] > rezultt[8] and rezultt[6] > rezultt[9]:
            rezult_list.append(f"   Высокий, по сравнению с остальными,G: Условный само - "
               f"контроль <<благодаря>> строгому воспитанию в атмосфере, где человек не должен"
               f"ни показывать никакого рода эмоции, ни выражать своего мнения. Самоанализ.")
# ======================================
        if rezultt[3] > rezultt[0] and rezultt[3] > rezultt[1] and rezultt[3] > rezultt[2] and\
            rezultt[3] > rezultt[6] and rezultt[3] > rezultt[4] and rezultt[3] > rezultt[5] and\
            rezultt[3] > rezultt[7] and rezultt[3] > rezultt[8] and rezultt[3] > rezultt[9]:
            rezult_list.append(f"   D выше, чем другие: Борется с жизнью и почти ничем не "
               f"занимается, кроме этого.Настоящее социальное положение позволяет хорошо "
               f"маскироваться и носить маску со мной ничего не может случиться")
# ======================================
        if rezultt[4] > rezultt[5]:
            rezult_list.append(f"   E={rezultt[8]} выше, чем F={rezultt[9]}: Человек делает больше, чем он смог бы сделать не напрягаясь.")

# ======================================
        if abs(rezultt[3]-rezultt[4])<5 and abs(rezultt[4]-rezultt[5])<5:
            rezult_list.append(f"   Расположенные в одну линию D, E, F, показывают, что человек"
                f" удерживает свою активность в рамках возможностей.")
# ======================================
        if rezultt[5] > rezultt[4]:
            rezult_list.append(f"   F выше, чем E: Не делает того, что мог бы сделать. Одитинг.")
# ======================================
        if rezultt[8] > rezultt[0] and rezultt[8] > rezultt[1] and rezultt[8] > rezultt[2] and\
            rezultt[8] > rezultt[3] and rezultt[8] > rezultt[4] and rezultt[8] > rezultt[5] and\
            rezultt[8] > rezultt[6] and rezultt[8] > rezultt[7] and rezultt[8] > rezultt[9]:
            rezult_list.append(f"   I выше остальных: Человек со слишком мягким сердцем.Легче всего назвать - «сосунок».")
# ======================================
        if rezultt[0] < -20 and rezultt[1] < -20 and rezultt[2] < -20:
            rezult_list.append(f"   A, B и C низкие: Невротичный.Отягощен прошлыми потерями.Часто "
                f"указывает на заброшенность в детстве. 1.Ups & Down. 2.Самоанализ.")
# ======================================
        if rezultt[0] < -20 and rezultt[4] > 40:
            rezult_list.append(f"   A низкий, E высокий: Рассеянный. Самоанализ.")
# ======================================
        if rezultt[0] < -20 and rezultt[1] < -20 and rezultt[2] < -20 and rezultt[4] > 40 :
            rezult_list.append(f"   Низкие A, B и C, высокий E: Личность, возможно склонная к самоубийству.")
# ======================================
        if rezultt[0] < -20 and rezultt[1] > 20 and rezultt[2] > 20 and rezultt[3] > 20 and \
                rezultt[4] > 20 and rezultt[5] > 20 and rezultt[6] > 20 and rezultt[7] > 20 \
                and rezultt[8] > 20 and rezultt[9] < -20:
            rezult_list.append(f"  A={rezultt[0]}, J={rezultt[9]} низкие: Если остаток графика"
              f" приемлемый, это показывает, что личность находится в среде с уровнем 1.1, которая"
              f" его подавляет и лишает возможности общаться, потому что это будет искажено"
              f" и использовано против него самого. Персональная целостность.")
# ================================================
        if rezultt[0] < -20 and rezultt[2] < -20 and rezultt[6] < -20 and rezultt[5] > 20:
            rezult_list.append(f"  A={rezultt[0]}, C={rezultt[2]}, G={rezultt[6]} низкие"
               f" F={rezultt[5]} высокий: Взрывное недовольство. Очень темпераментен.")
# =====================================
        if rezultt[0] > 20 and rezultt[7] < -20:
            rezult_list.append(f"  A={rezultt[0]} высокий, H={rezultt[7]} низкий:  "
                               f"«само совершенство».")
# ====================================
        if rezultt[0] > 30 and -20 < rezultt[3] < 20:
            rezult_list.append(f"  Высокий A={rezultt[0]}, D={rezultt[3]} средний: Индивидуальный"
              f" расчет на стабильные данные, нежели на личную уверенность. Здесь «Интеллектуальное"
              f" понимание». Большинство студентов будут додумывать данные, если они не подходят "
              f"для них.")
# =====================================
        if rezultt[1] < -20 and rezultt[6] < -20 and rezultt[5] > 20:
            rezult_list.append(f"  B={rezultt[1]}, G={rezultt[6]} низкие"
               f" F={rezultt[5]} высокий: Чувство неполноценности. Одитинг.")
# =====================================
        if rezultt[1] > 20 and rezultt[3] < -20:
            rezult_list.append(f"  B={rezultt[1]} высокий, D={rezultt[3]} низкий:  "
              f"Склонный к манику безумного веселья.")
# =====================================
        if  rezultt[5] >= 70 and rezultt[6] < 20:
            rezult_list.append(f"  F1 G3-4 Вы безответственны в жизни и работе.Вы обвиняете других"
            f" в ваших проблемах, причем не принимаете во внимание то, что сами несете какую"
            f"- то ответственность за то, что случилось или случится.тот факт, что Вы достаточно"
            f" способный и открытый человек, но еще и безответственный, говорит, что Вы способны" 
            f" делать что - то без учета последствий.Это очень опасная позиция, и Вы попадете в беду,"
            f" если еще не попали. Персональная целостность.")
# =============================================
        if  rezultt[6] >= 70 and rezultt[5] < 20:
            rezult_list.append(f" G1 F3-4 Вы не очень способный и открытый человек.Вы почти не "
            f"способны правильно воспринимать людей и ситуации.Хотя Вы и рассматриваете себя,"
            f" как личность довольно ответственную и причинную, это не совсем так.В некоторых"
            f" нестандартных ситуациях Вы берете на себя ответственность, но так как Вы"
            f" предпочитаете тщательно следить за тем, что делаете, Вы сталкиваетесь с"
            f" трудностями.Но чем лучше Вы следите за своими шагами, тем легче Вам"
            f" преодолевать трудности.")
# ==============================================
        if rezultt[7] >= 70 and rezultt[8] < 20:
            rezult_list.append(f"  H1 I3-4 Вы не способны быть эмпатичным, так как не можете"
               f" представить себя на месте другого и следовательно понять его взгляды на вещи и"
               f" ситуацию. из-за этого Вы не настолько хороши, насколько бы Вам хотелось. Вы"
               f" пытаетесь быть откровенным, но только поверхностно. В действительности недостаток"
               f" понимания - это очень плохо, и Вы только притворяетесь, что видите в этом"
               f" хорошую сторону.")
# =================================================
        if rezultt[8] >= 70 and rezultt[7] < 20:
            rezult_list.append(f"  I1 H3-4 Вы чрезвычайно критичны.Вы атакуете словами и "
            f"давите0 на психику, причем подло и со злостью.Вы думаете, что можете смотреть с "
            f"точки зрения и позиции других людей, но в действительности это только притворство,"
            f" так как по - настоящему Вы видите только плохие стороны в других людях и в своем"
            f" окружении.Возможно, Вы довольно жесткий человек. Ups & Down.")
# ======================================
        if rezultt[3] >= 70 and rezultt[0] < 20:
            rezult_list.append(f"  D1 A3-4 У Вас неуравновешенный характер, а также Вы слишком "
              f"импульсивны и рассеяны. Вы не способны концентрировать ваше внимание, которое либо"
              f" блуждает где-то, либо вынужденно закреплено. Вы ложно рассматриваете себя, как"
              f" совершенно зависимого человека, но такая зависимость и уверенность основана на"
              f" гипнотических решениях, суждениях и мнениях, которые Вы не можете ни"
              f" контролировать, ни изменить. Самоанализ.")
# ======================================
        if rezultt[4] >= 70 and rezultt[3] < 20:
            rezult_list.append(f"  E1 D3-4 Вы независимы, но лишь в некоторой степени уверены в "
              f"себе. Вы действительно не решили для себя, что Вам нужно, а что нет, к тому же"
              f" Вы очень активны. Однако, не все ваши действия под вашим контролем, так как Вы"
              f" не знаете, чего хотите добиться своей деятельностью. Вы понимаете, что что-либо"
              f" делать гораздо лучше, чем ничего, но работа впустую (без какой-либо цели)"
              f" неприятна для Вас.")
# =======================================
        if rezultt[4] >= 70 and rezultt[5] < 20:
            rezult_list.append(f"  E1 F3-4 Вы человек сдержанный и боитесь встретиться с "
              f"управлением людьми и ситуациями, где не все ясно. Это создает для Вас множество"
              f" неприятностей. То, что Вы активны, а иногда одержимы, показывает, что Вы делаете"
              f" вещи, которые в действительности выше ваших возможностей. Результатом будут"
              f" множество неприятностей в будущем.")
# ===================================
        if rezultt[5] >= 70 and rezultt[4] < 20:
            rezult_list.append(f"   F1 E3-4 Вы не очень активны. Вам трудновато решать проблемы "
              f"на ходу и продолжать их, однажды начав. но Вы очень способный и открытый человек,"
              f" и можете управлять как людьми, так и ситуациями. Вы, из-за своей великой лени,"
              f" не идете на все, что действительно способны сделать и зарываете свои таланты.")
# =====================================
        if rezultt[1] >= 70 and rezultt[0] < 20:
            rezult_list.append(f"   B1 A3-4 Так как у Вас некоторые проблемы с концентрацией "
              f"внимания, а также у Вас импульсивный и неуравновешенный характер, Вы не счастливый"
              f" человек, или чувствуете себя таким. Ваша ненадежность, вероломство и то, что Вы"
              f" не цените оказанного Вам доверия, огорчают окружающих. Поэтому ваш энтузиазм и"
              f" интерес к жизни значительно понижаются. Самоанализ.")
# =============================================
        if rezultt[1] >= 70 and rezultt[2] < 20:
            rezult_list.append(f"   B1 C3-4 Вам легко сохранить самообладание и расслабиться, "
              f"что не позволяет Вам чувствовать себя таким счастливым, как обычно. Ваша привычка"
              f" нервничать уменьшает энтузиазм и понижает интерес к жизни больше, чем Вы"
              f" предполагаете. Вас слишком легко разволновать и раздразнить, это не дает"
              f" поддерживать Вам оптимистическое настроение. При таком воздействии на Вас у"
              f" Вас падает сила духа. Одитинг.")
# ===============================================
        if rezultt[2] >= 70 and rezultt[0] < 20:
            rezult_list.append(f"   C1 A3-4 Вы неуравновешенны и рассеяны. Вы практически не"
              f" можете контролировать свое внимание, которое либо блуждает где-то, либо занято"
              f" какой-то одной проблемой. из-за этого Вы не настолько спокойны, насколько Вас"
              f" хотелось бы, чтобы о Вас думали. Ваше спокойствие - это тот внешний лоск, за"
              f" который Вы пытаетесь спрятать вашу нестабильность и ненадежность. Самоанализ.")
# ==================================================
        if rezultt[2] >= 70 and rezultt[1] < 20:
            rezult_list.append(f"   C1 B3-4 Вы не совсем довольны жизнью. Это делает Вас намного "
              f"более нервным, чем Вы думаете. Ваши проблемы и трудности, которые являются "
              f"источниками вашей депрессии, приводят к внутреннему расстройству, которое Вы"
              f" отчаянно пытаетесь скрыть при помощи внешнего проявления спокойствия и "
              f"безмятежности. Ваши усилия проявить самообладание быстро рушатся, если не"
              f" приводят к решению проблем. Одитинг.")
# =============================================
        if rezultt[6] >= 90 and rezultt[8] >= 90:
            rezult_list.append(f"    90 G, +90 I ? Мученик или страдает комплексом преследования."
                               f"Человек скорее всего врет.")
# ==============================
        if rezultt[0] >= 70 and rezultt[1] < 20:
            rezult_list.append(f"   A1 B3-4 Вы подавлены и несчастливы, смотрите на жизнь с "
               f"пессимистической точки зрения. Для Вас существует слишком много проблем и "
               f"трудностей, чтобы управлять ими. Это вызывает бедность ваших суждений и недоверие,"
               f" причем активизирует вашу способность концентрироваться, хотя Вы считаете это как"
               f" одну из ваших лучших характеристик. Ваша семья и друзья считают, что из-за этого"
               f" с Вами трудно общаться.")
# ===============================
        if rezultt[0] >= 70 and rezultt[2] < 20:
            rezult_list.append(f"   A1 C3-4 Вы человек нервный и очень возбужденный. Ваши "
              f"беспокойства и волнения плохо влияют не только на окружающих, но и на Вас самих."
              f" Ваша неспособность расслабиться и постоянное состояние нервозности приводят к"
              f" неуравновешенности, понижают вашу способность концентрироваться. Это влияет на"
              f" скупость ваших суждений и приводит к непостоянству в решениях, хотя Вы смотрите"
              f" на это, словно Вы достаточно справедливы в этих вопросах. Одитинг.")
# ==============================

    with open(name_fileTXT, "w", encoding='utf-8') as file:
        for line in rezult_list:
            file.write(textwrap.fill(line, 60) + '\n')

    return rezult_list


# # print result
# for yy in test_decipher(rezultt, f"graph_fold\\Ttest"):
#     print(textwrap.fill(yy, 80))
#


# with open(r"D:\test.txt", "w") as file:
#     for line in test_decipher(rezultt):
#         file.write(textwrap.fill(line,60)+ '\n')
# xx, yy = 1, 0
# test_decipher(rezultt,'tit.txt',xx ,yy )