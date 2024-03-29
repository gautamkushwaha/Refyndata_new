#filter a list which is divisible by some number sa 13

my_list = [12,13,14, 15, 26, 36]

result = list(filter(lambda x: (x % 13 ==0), my_list ))

print(result)


dec = 400
char ="p"

h = hex(dec)
b = bin(dec)
o = oct(dec)
print(f"{h} , {b}, {o}")

print(ord(char))