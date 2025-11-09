son = int(input("Son kiriting: "))
yigindi = 0

while son > 0:
    raqam = son % 10
    yigindi += raqam
    son //= 10

print("Raqamlar yig'indisi:", yigindi)
