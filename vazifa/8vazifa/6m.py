# Kirish: Berilgan son 3 ga va 5 ga bo‘linish-bo‘linmasligini tekshiring.
# Chiqish: Agar har ikkala shart bajarilsa "3 va 5 ga bo‘linadi", 
# faqat 3 ga bo‘linadigan bo‘lsa "Faqat 3 ga bo‘linadi",
#  faqat 5 ga bo‘linadigan bo‘lsa "Faqat 5 ga bo‘linadi", 
# hech biriga bo‘linmasa "Bo‘linmaydi" deb ekranga chiqaring.

# Tizim!

son=int(input('Please enter number = '))
a=3
b=5
if son%a==0 and son%b==0:
    print('Siz kiritgan son 3 va 5 ga bolinadi!')
elif son%a==0 and son%b!=0:
    print('Sizning soningiz faqat 3 ga bolinar ekan!')
elif son%b==0 and son%a!=0:
    print('siznning soningiz faqat 5ga bolinar ekan!')
else:
    print('Siz kiritgan son 5 ga ham 3 ga ham bolinmas ekan! Qayta urining!')    