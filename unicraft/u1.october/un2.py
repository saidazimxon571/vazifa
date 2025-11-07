distance=float(input("Masofani kiriting = "))
speed=float(input("Tezlikni kiriting = "))
if speed <=0:
    print("Tezlik 0 ga yoki undan kichik songa ega bolishi mumkun emas iltimos boshqa raqam kiriting!")
else:
    time=distance/speed
    hours=int(time)
    minutes=int((time-hours)*60)
    seconds=int(((time-hours)*60-minutes)*60)
    print(f"bu taxminan {hours} soat {minutes} minut {seconds} sekund vaqt oladi")