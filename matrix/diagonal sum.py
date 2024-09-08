def diagonalsum(matrix:list[list[int]])->int:
    dia1=0
    dia2=0
    n=len(matrix)-1
    for i in range(len(matrix)):
        dia1+=matrix[i][i]
        dia2+=matrix[n-i][n-i]
    return print(f'diagonal sum {dia1}, diagonal sum2 {dia2}')

matrix=[
    [1,2,3,10],
    [4,5,6,10],
    [7,8,9,10],
    [10,10,10,10]
]

diagonalsum(matrix)