# calculate the factorial of a number using recursion
# factorial of  5 = 5 * 4 * 3 * 2 * 1
# factorial of 0 or 1 is 1

def rec_fact(num):
    if (num == 1 or num == 0):
        return num
    else:
        return (num * rec_fact(num-1))

number = 5

print(rec_fact(number))