class Solution {
public:
    int up(int row, int col, int m, int n, vector<vector<int>>& obstacleGrid,
           vector<vector<int>>& dp) {
        if (row == m || col == n)
            return 0;
        if (obstacleGrid[row][col] == 1)
            return 0;
        if (row == m - 1 && col == n - 1)
            return 1;
        if (dp[row][col] != -1)
            return dp[row][col];
        return dp[row][col] = up(row + 1, col, m, n, obstacleGrid, dp) +
                              up(row, col + 1, m, n, obstacleGrid, dp);
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return up(0, 0, m, n, obstacleGrid, dp);
    }
};
