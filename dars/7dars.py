# a=int(input("raqam yoz = "))
# if a%2==0:
#     print("fizzz")
# else:
#     print("bizz")

# print("b") if fg>r else print("yaxuuu")
ages=input("(12,13) yozib bering:")
# print(ages)
group_age_list=ages.split(',')
sonli_list=[]
for age in group_age_list:
    age=int(age)
    sonli_list.append(age)
    s=age+age

toifa=f"Yosh toifasi:{set(sonli_list)}"



