class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    grid[i][j]=1
                    continue
                grid[i][j]+=grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]
