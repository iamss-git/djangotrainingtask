def TransposeMatrix(matrix):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            result[j][i]=matrix[i][j]

X=  [[1,2],
     [3,4],
     [5,6],
     [7,8]]

result= [[0,0,0,0],
         [0,0,0,0]]
TransposeMatrix(X)
for r in result:
       print(r)
