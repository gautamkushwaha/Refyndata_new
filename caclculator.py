# calculator: sum, sub, mul, div

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x // y

num1 = 10
num2 = 20
operation = int(input("Enter the operations: 1-add, 2-sub, 3-mul, 4- div: "))

if(operation == 1):
    print(add(num1, num2))
    
elif(operation == 2):
    print(sub(num1, num2))
    
elif(operation == 3):
    print(mul(num1, num2))
    
elif(operation == 4):
    print(div(num1, num2))

else:
    print("Invlaid inputs")