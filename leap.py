# to be a leap year a year should be divided by 4oo year and 100 year and also should be divided by 4 and 100 year

year = 2004

if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 == 0 ) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")