class Solution {
public:
    int fib(int n) {
        if(n <= 1)
            return n;
        vector<int>dp(n+1,-1);
        for(int i = 0; i < n+1 ; i++){
            if(i <= 1)
                dp[i] =  i;
            else
                dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
};