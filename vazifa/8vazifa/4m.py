year=int(input('Please enter random year = '))

if (year%4==0 and year%100!=0) or (year%400==0):
    print("This year is Kabisa year")
else:
    print("This year is not Kabisa year")
 