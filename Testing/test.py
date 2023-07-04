##########################################

# from mess import Mod

# a,b = Mod()
# print(a,b)

# def A():
#     def B():
#         a = "123"
#         b = 321
#         return a,b
#     B()
#     c,d = B()
#     return c,d

# A()
# z,x = A()
# print(z,x)

##########################################

# class final:
#     def __init__(self,item,lvl):
#         self.item = item
#         self.lvl = lvl

##########################################

# import time

# def waiting():
#     for i in range(20):
#         for ch in ["擷取中-", "擷取中\\", "擷取中|", "擷取中/"]:
#             print("\r%s"%ch, end="",flush=True)
#             time.sleep(0.2)

# waiting()

##########################################

# import threading
# import time

# def job():
#   for i in range(5):
#     print("Child thread:", i)
#     time.sleep(1)

# t = threading.Thread(target = job)
# t.start()

# for i in range(1):
  # for ch in ["擷取中-", "擷取中\\", "擷取中|", "擷取中/"]:
  #     print("\r%s"%ch, end="",flush=True)
  #     time.sleep(0.2)

# if t.join():
#   print("Done.")
# else:
#   for i in range(1):
#     for ch in ["擷取中-", "擷取中\\", "擷取中|", "擷取中/"]:
#         print("\r%s"%ch, end="",flush=True)
#         time.sleep(0.2)

# t.join()
# print("save")

##########################################

# from openpyxl import Workbook, load_workbook
# from openpyxl.utils import get_column_letter

# wb = load_workbook('shop.xlsx')
# ws = wb['ID']

# f = open("ID.txt", 'w', encoding=" UTF-8")

# for row in range(2,5081):
#   for col in range(1,2):
#     char = get_column_letter(col)
#     # print(ws[char + str(row)].value)
#     f.write('{\n"id": "%s",\n'%ws[char + str(row)].value)
#     for col in range(2,3):
#       f.write('"text": "%s",\n},\n'%ws[char + str(row)].value)

##########################################

# import time

# print("Loading",end = "")
# for i in range(20):
#     print(".",end = '',flush = True)
#     time.sleep(0.5)

##########################################
# import datetime

# loc_dt = datetime.datetime.today() 
# loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
# print(loc_dt_format)

# time_del = datetime.timedelta(hours=3)
# new_dt = loc_dt + time_del 
# datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
# print(datetime_format)

##########################################
# test = [[0 for i in range(2)] for j in range(10)]
# a = 0

# for i in range(1,len(test)):
#   test[a][0] = i
#   test[a][1] = i+10
#   a += 1

# for row in test:
#   print(f'A = {row[0]}, B = {row[1]}')

##########################################
# import linecache

# total = 19
# num = 10
# with open(f'./Discord/QA/205553731972890625.txt', 'r', encoding = 'utf8') as f:
#   for i in range(total, total-num, -1):
#     print(linecache.getline('./Discord/QA/205553731972890625.txt', i))

##########################################
# str = "卡蘭德 /公開倉庫 /超過 99 筆資料"
# str1 = "/"

# print(str[:str.index(str1)])

# numbers = [int(temp)for temp in str.split() if temp.isdigit()]
# print(numbers)

##########################################
