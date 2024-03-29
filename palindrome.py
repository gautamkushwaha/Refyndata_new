# palindrome is a string which is same from start and end

my_string = "abcdcba"

my_string = my_string.casefold()

rev_string = reversed(my_string)

if (list(rev_string) == list(my_string)):
    print(" The  string is a palindrome")
else:
    print(" The string is not a palindrome")

