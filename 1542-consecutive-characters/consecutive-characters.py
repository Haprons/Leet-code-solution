class Solution:
    def maxPower(self, s: str) -> int:
        temStr = s[0]
        res = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                temStr = temStr + s[i]
                if len(temStr) > res:
                    res = len(temStr)
            else:
                temStr = s[i]
        return res