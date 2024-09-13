def matMul(matrix1:list[list[int]],matrix2:list[list[int]])->list[list[int]]:

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j]+=matrix2[i][j]
    
mat1=[[1,2,3],
      [4,5,6],
      [7,8,9]]

mat2=[[1,2,3],
      [4,5,6],
      [7,8,9]]

matMul(mat1,mat2)

print(mat1)