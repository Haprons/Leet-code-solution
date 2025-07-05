class Solution {
public:
    int MPS(int row, int col, int m, int n, vector<vector<int>>& grid, vector<vector<int>>& dp) {
        if (row == m || col == n)
            return INT_MAX;  // Out of bounds
        
        if (row == m - 1 && col == n - 1)
            return grid[row][col];  // Destination
        
        if (dp[row][col] != -1)
            return dp[row][col];  // Memoized
        
        // If at last row, can only go right
        if (row == m - 1)
            return dp[row][col] = grid[row][col] + MPS(row, col + 1, m, n, grid, dp);
        
        // If at last column, can only go down
        if (col == n - 1)
            return dp[row][col] = grid[row][col] + MPS(row + 1, col, m, n, grid, dp);

        // General case
        return dp[row][col] = grid[row][col] + 
                              min(MPS(row + 1, col, m, n, grid, dp), 
                                  MPS(row, col + 1, m, n, grid, dp));
    }

    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return MPS(0, 0, m, n, grid, dp);
    }
};
