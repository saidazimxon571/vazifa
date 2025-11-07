# Kirish: Foydalanuvchidan 3 ta son kiritishini so‘rang.
# Chiqish: Eng katta sonni ekranga chiqaring.


yakka=[]

sonlar = []

for i in range(3):
    sonlar.append(input(f"{i+1} - sonni kiriting: "))

_max=max(sonlar)
print(_max)
