# convert decimal to binary using recursion

def convertToBinary(num):
    if num> 1:
        convertToBinary(num // 2)
        
    print(num%2, end='' )
    
#decimal number
dec = 34

convertToBinary(dec)
print()
        