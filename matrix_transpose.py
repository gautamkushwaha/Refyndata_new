# transpose of a matrix 

x = [[2, 3],
     [5,6],
     [7,8]]

result= [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]


for r in result:
  print(r)
  

resu = [[0, 0, 0],
        [0, 0, 0],]

for i in range(len(x)):
    for j in range(len(x[0])):
        resu[j][i]= x[i][j]
        
for element in resu:
    print(element)