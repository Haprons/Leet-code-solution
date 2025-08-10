class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        for c in 'aeiou':
            if c in s:
                count += 1
        return count > 0