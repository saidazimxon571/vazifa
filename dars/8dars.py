# dars=['english', 'tarix', 'matematika']
# fruit=['aple', 'banana','chery']

# for x in dars:
#     for y in fruit:
#         print(x,y)
# for x in dars:
#     if x == 'tarix':
#         continue
#     print(x)


# i=1
# while i<6:
#     i+=1
#     if i==3:
#         continue
#     print(i)

# menu={
#     'osh':30000,
#     'choy':5000,
#     'salat':10000,
#     'shashlik':20000
# }

# zakaz=[]
# menu_list=list(menu.keys())
# while True:
#     buyurtma=input(f"{menu_list} lardan tanlang(stop):")
#     if buyurtma=='stop':
#         break
#     if not buyurtma in menu:
#         print(f"Bizda {buyurtma} yo'q")
#         continue
#     print(f"{buyurtma} buyurtmangizga qo'shildi")
#     zakaz.append(buyurtma)

# print(zakaz)


# jami=0
# for z in zakaz:
#     if z in menu:
#         jami+=menu[z]
# answer=f"Sizda {jami} so'm bo'ldi"
# print(answer)


# cars=['onix','byd','tico']

# cars=['onix','byd','gentra','tico']

# cars_data={}
# while cars:
#     car=cars.pop()
#     price=input(f"{car}ning narxi:")
#     cars_data[car]=price
#     print(cars_data)
#     pr=cars_data.values()
# # enga=min(pr)
# # engq=max(pr)
# # if enga==cars_data:
# #       print(f'eng arzon mashina {cars_data}')
# # if engq==cars_data:
# #      print(f'eng qimmat mashina {cars_data}')
# max_price=max(list(cars_data.values()))
# min_price=min(list(cars_data.values()))
# # print(max_price)
# for k,v in cars_data.items():
#     if v==max_price:
#         print(f"Eng qimmati {k}")
#     elif v==min_price:
#         print(f"Eng arzoni {k}")

# import random

# son=random.randint(1,100)
# while True:
   
     