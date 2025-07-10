class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = int((-1 + math.sqrt(1 + 4 * (n*2))) // 2)
        return r