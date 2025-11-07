import random
son=random.randint(1,100)
while True:
     user_ansver=int(input('Kampiyuter oylagan sonni topib yozing = '))
     if user_ansver>100:
         print('iltimos 0 dan 100 gacha bolgan son kiriting :)')

     qoshish=son-user_ansver
     ayrish=user_ansver-son

     if son>user_ansver:
         print(f'topolmadiz {user_ansver}ga yana {qoshish} ni qoshsangiz togri boladi')
     elif user_ansver>son:
         print(f'topolmadiz {user_ansver}dan yana {ayrish} ni ayirsangiz togri boladi')
     else:
         print("Qoyil topdiz !")
         break
  