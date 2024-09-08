def rowsum(matrix:list[list[int]])->list[int]:
    answer=[]
    colsum=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            colsum+=matrix[i][j]
        answer.append(colsum)
        colsum=0
    return print(answer)


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]


rowsum(matrix)