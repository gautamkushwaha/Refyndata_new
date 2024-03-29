# python program to find sum of natural numbers using recursion

def sum_natRec(num):
    if num <= 1:
        return num
    else: 
        return (num + sum_natRec(num - 1))
    
    
    
number = int(input("Enter the number: "))

print(f"The sum of numbers upto {number} is : ", sum_natRec(number))