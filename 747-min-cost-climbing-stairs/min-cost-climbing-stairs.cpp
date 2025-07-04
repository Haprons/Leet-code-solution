class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n= cost.size();
        vector<int>dp(n,0);
        int prev = cost[0];
        int curr = cost[1];
        int next;
        for(int i = 2 ; i < n ; i++ )
        {
            next = cost[i] + min(prev,curr);
            prev = curr;
            curr = next;
        }
        return min(curr,prev);
    }
};