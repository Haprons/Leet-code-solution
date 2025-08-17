class Solution {
    public int closedIsland(int[][] grid) {
        int count=0;
        int m = grid.length;
        int n = grid[0].length;

        //Sink the islands which are connected to edge
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if((i==0 || i==m-1 || j==0 || j==n-1) && grid[i][j]==0){
                    dfs(grid, i,j);
                }
            }
        }

        //Count the remaining islands
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(grid[i][j]==0){
                    dfs(grid,i,j);
                    count++;
                }
            }
        }
        return count;
    }
    public void dfs(int grid[][], int i, int j){
        if(i<0 || i>=grid.length || j<0 || j>=grid[0].length || grid[i][j]==1){
            return ;
        }
        grid[i][j]=1;
        dfs(grid,i+1,j);
        dfs(grid,i-1,j);
        dfs(grid,i,j+1);
        dfs(grid,i,j-1);
    }
}