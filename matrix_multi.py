# multiplication of matrixs: matrix should have same number of column and another should have that number of row

x = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

z = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j]=   z[i][j] + x[i][k] * y[k][j]
            
for element in z:
    print(element)