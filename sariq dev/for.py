# # dickt
# bu malumot turida hech qachon ozgaruvchan malumot turlari key bola olmaydi  asosiy qoida shu!
# agr ozgaruvchan malumot turlari kiritilsa u key eror beradi
# di={
#     'name':'Abror',
#     20:'pul',
#     80.5:"vazn"
# }
# for i in di:
#     print(i,di[i])
# for k,v in di.items():
#     print(v,k)
# for luboy in di.values():
#     print(luboy)
# val=tuple(di.values())
# print(di)
# print(val)
di={
    'non':4500,
    'qoy':5000,
    'yog':100000
}
narxl=list(di.values())
narx=min(narxl)
for k,v in di.items():
    if v==narx:
        print(f"eng qimmat mahsulot = {k}")