class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0
        l = ['a','e','i','o','u']
        for c in s:
            if c in l:
                count += 1
        return count > 0