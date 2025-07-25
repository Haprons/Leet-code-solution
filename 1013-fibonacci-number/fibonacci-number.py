class Solution:
    def fib(self, n: int) -> int:
        dp = []
        if n <= 1:
            return n
        for i in range(n+1):
            if i <= 1:
                dp.append(i)
            else:
                dp.append(dp[i-1] + dp[i-2])
        return dp[n]