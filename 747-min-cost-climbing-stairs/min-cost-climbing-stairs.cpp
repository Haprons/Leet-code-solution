class Solution {
public:
    int CS(int i,vector<int>& cost,vector<int>&dp) 
    {
        if(i>=cost.size()) return 0;
        if(dp[i] != -1) return dp[i];
        return dp[i] = cost[i] + min(CS(i+1,cost,dp),CS(i+2,cost,dp));
    }
    int minCostClimbingStairs(vector<int>& cost){
        int n = cost.size();
        vector<int>dp(n,-1);
        return min(CS(0,cost,dp),CS(1,cost,dp));
    }
};