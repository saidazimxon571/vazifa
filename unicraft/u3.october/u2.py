age=int(input("Yoshingizni kiriting = "))
gol=int(input("Gollar sonini kiriting = "))
if age<=18 and gol>0:
    print("yosh istedod")
elif age<=18 and gol<1:
    print("oz ustingda sihla")
elif age<=35 and gol>=3:
    print("Bolajak yulduz")
elif age<=35 and gol<3:
    print("Oddiy futbolchi")
elif age>35 and gol>=1:
    print("Maglubiyatsz veteran!")
else:
    print("Tajribali murabbiy")          