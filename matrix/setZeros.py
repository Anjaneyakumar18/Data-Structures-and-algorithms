'''
1 0 1 1     0 0 0 0
2 3 4 5     2 0 4 5
2 3 4 5     2 0 4 5

'''

def SetZeros(matrix:list[list[int]])->list[list[int]]:


    zero_ind=[]
    rows=len(matrix)
    col=len(matrix[0])


    for i in range(rows):
        for j in range(col):
            if matrix[i][j]==0:
                zero_ind.append([i,j])
    

    for coordinates in zero_ind:

        for i in range(coordinates[0]):
            matrix[i][coordinates[1]]=0

        for i in range(coordinates[0],rows):
            matrix[i][coordinates[1]]=0

        for i in range(coordinates[1]):
            matrix[coordinates[0]][i]=0
            
        for i in range(coordinates[1],rows):
            matrix[coordinates[0]][i]=0


    return None

matrix=[[1,0,2,3,4],
        [2,3,4,5,6],
        [7,8,5,3,5],
        [2,5,7,3,8],
        [5,9,2,5,8]]

SetZeros(matrix)

print(matrix)