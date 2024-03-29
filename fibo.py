#fibonacci sequences are 0, 1, 1, 2, 3, 5, 8,...... ((n-1) + (n-2))


# f3 = f2 + f1( nth term = (n-1)th term + (n-2)th term

def rec_fib(num):
    if num <= 1:
        return num
    else:
        return (rec_fib(num - 1) + rec_fib(num - 2))
    

nterms = int(input("Enter the number of terms: "))
for i in range(nterms):
    print(rec_fib(i))