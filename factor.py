# to find a factor of a number 
# 4 = 1, 2, 4


def factor(num):
    for i in range(1, num+1):
       if num % i == 0:
           print(i)
           
           
factor(60)
        