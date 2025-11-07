baho={

}
name=input("Oquvchi ismini kiriting = ")
grade=int(input("oquvchi bahosini kiriting = "))
baho[name]=grade
for k,v in baho.items():
    if v>89:
        print('Juda yaxshi oqiyabdi!')
    else:
        print('yomon emas lekin yaxshilash kerak!')
        