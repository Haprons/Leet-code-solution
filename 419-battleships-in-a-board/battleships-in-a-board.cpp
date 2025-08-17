class Solution {
public:
    void DFS(int i,int j,vector<vector<char>>& board){
        if(i>=board.size()||i<0||j>=board[0].size()||j<0||board[i][j]!='X'){
            return ;
        }
        board[i][j]='.';
        DFS(i+1,j,board);
        DFS(i-1,j,board);
        DFS(i,j+1,board);
        DFS(i,j-1,board);
    }
    int countBattleships(vector<vector<char>>& board) {
        int ans=0;
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(board[i][j]=='X'){
                    ans++;
                    DFS(i,j,board);
                }
            }
        }
        return ans;
    }
};