class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter
        count = Counter(basket1) - Counter(basket2)
        count += Counter(basket2) - Counter(basket1)
        if any(v % 2 for v in count.values()): return -1

        extra = []
        min_val = min(basket1 + basket2)
        for k, v in count.items():
            extra += [k] * (v // 2)
        extra.sort()
        return sum(min(x, 2 * min_val) for x in extra[:len(extra)//2])