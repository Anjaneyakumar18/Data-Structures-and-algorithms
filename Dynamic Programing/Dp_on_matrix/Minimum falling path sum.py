class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows,cols=len(matrix),len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if i==0:
                    continue
                elif j==0:
                    if cols>1:
                        matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                    else:
                        matrix[i][j]+=matrix[i-1][j]
                elif j==cols-1:
                    if cols>1:
                        matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j])
                    else:
                        matrix[i][j]+=matrix[i-1][j]
                else:
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
        return min(matrix[-1])

        
