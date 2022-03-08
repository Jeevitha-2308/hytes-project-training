year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("leap year",year)
elif (year % 4 ==0) and (year % 100 != 0):
    print("not an leap year",year)
else:
    print(" not a leap year",year)
