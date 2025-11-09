balance = 100000

print("Pul yechish tizimiga xush kelibsiz!")

try:
    sorov = int(input("Nechta pul yechmoqchisiz? "))

    if sorov > balance:
        raise ValueError("Hisobda yetarli mablag' yo'q.")
    else:
        balance -= sorov
        print(f"Pul muvaffaqiyatli yechildi. Yangi balans: {balance} so'm.")

except ValueError as e:
    print(f"Xatolik: {e}")

finally:
    print(f"Jarayon tugadi. Joriy balans: {balance} so'm.")
