

# compute the hcf of a two numbers

def compute_hcf(x, y):
    while(y):
        x, y = y, x%y
    return x

def compute_lcm(x, y):
    lcm = (x * y) // compute_hcf(x, y)
    return lcm


# hcf = compute_hcf(200,19)
# print(hcf)

lcm = compute_lcm(500, 500)
print(lcm)