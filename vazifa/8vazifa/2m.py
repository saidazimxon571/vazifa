# Kirish: Foydalanuvchidan baho (0 dan 100 gacha) kiritishini so‘rang.
# Chiqish: Agar baho 90 dan yuqori bo‘lsa "A",
#  80-90 oralig‘ida "B",
#  70-80 oralig‘ida "C", 
# 60-70 oralig‘ida "D",
#  60 dan past bo‘lsa "F" bahosini ekranga chiqaring.
# Baholash Tizimi!
baho=int(input('Please enter grade of student = '))
if baho>100:
    print('please enter until 100 grade!')
elif baho >=90:
    print('Your rank is  A')
elif baho>=80 and baho <90:
    print('Your rank is  B')
elif baho>=70 and baho <80:
    print('Your rank is  C')
elif baho>=60 and baho <70:
    print('Your rank is  D')
else:
    print('Your rank is  F')
