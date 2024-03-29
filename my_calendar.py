# print calendar of a given month and year

import calendar

yy = 2024



# display the calendar
for mm in range(1, 13): 
  print(calendar.month(yy,mm))


# Program to display calendar of the given month and year

# # importing calendar module
# import calendar

# yy = 2014  # year
# mm = 11    # month

# # To take month and year input from the user
# # yy = int(input("Enter year: "))
# # mm = int(input("Enter month: "))

# # display the calendar
# print(calendar.month(yy, mm))