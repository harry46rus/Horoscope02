# # import schedule
# from schedule import *
# import schedule
# import time
#
# def job():
#     print("I'm working...")
#
# # Run job every 3 second/minute/hour/day/week,
# # Starting 3 second/minute/hour/day/week from now
# # schedule.every(10).seconds.do(job)
#
# # job()
#
# # for i in range(100):
# #      time.sleep(3)
# #      # main()
# #      job()
#
# while True:
#     time.sleep(3)
#     # main()
#     job()

dd={"30.07.2022": ["Доллар США","61,3101","Евро","62,5695"]}
x=dd.keys()
print(x,dd.items())

for key, value in dd.items():
        print(key, value[0],value[1],value[2],value[3])
# print(dd, dd.get(x))
x = 10
w =500