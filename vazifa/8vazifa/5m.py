 # Kirish: Foydalanuvchidan parol so‘rang.
 # Chiqish: Agar parol "12345" ga teng bo‘lsa "Xush kelibsiz!", 
 # aks holda "Noto‘g‘ri parol" deb ekranga chiqaring.

# PArol

code=int(input('Please enter your code = '))
r_code=12345
if code==r_code:
    print('Your code is perfect! ')
else:
    print('Your code is not perfect! ')