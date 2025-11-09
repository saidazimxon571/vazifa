mh={
    'non':4000,
    'olma':5000,
    'qovun':8000,
    'yog':10000
}
so=input("Mahsulot nomini kiriting = ")
for k,v in mh.items():
    if k==so:
        print(v)
    else:
        print("Unday mahsulot bizning dokonda topilmadi SORRY !")