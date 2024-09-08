def colsum(matrix:list[list[int]])->list[int]:
    colsum=0
    answer=[]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            colsum+=matrix[j][i]
        answer.append(colsum)
        colsum=0
    return print(answer)

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

colsum(matrix)