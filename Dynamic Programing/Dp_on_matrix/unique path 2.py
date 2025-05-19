class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int row = obstacleGrid.length;
        int col = obstacleGrid[0].length;
        int[][] grid = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (obstacleGrid[i][j] == 1) {
                    grid[i][j] = 0;
                } else if (i == 0 && j == 0) {
                    grid[i][j] = 1;
                } else if (i == 0) {
                    grid[i][j] = grid[i][j - 1]; 
                } else if (j == 0) {
                    grid[i][j] = grid[i - 1][j]; 
                } else {
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]; 
                }
            }
        }

        return grid[row - 1][col - 1];
    }
}
