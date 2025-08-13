class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return (n * n if n * n <= maxWeight // w else maxWeight // w)