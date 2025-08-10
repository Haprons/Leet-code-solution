class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        if len(complexity) <= 1:
            return 1
        first = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= first:
                return 0
        mod = 10**9 + 7
        ans = 1
        for j in range(1, len(complexity)):
            ans = (ans * j) % mod
        return ans