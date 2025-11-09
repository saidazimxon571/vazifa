import random
son=random.randint(1,100)
while True:
     user_ansver=int(input('Kampiyuter oylagan sonni topib yozing = '))
     if user_ansver>100:
         print('iltimos 0 dan 100 gacha bolgan son kiriting :)')
     if user_ansver>son:
         print('kichikroq son kiriting toplmadingiz :(')
     elif user_ansver<son:
         print('kottaroq son kiriting Topolmadingiz :(')
     else:
         print('Qoyil topdiz :)')
         break