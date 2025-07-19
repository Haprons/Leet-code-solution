class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in set(t):
            if s.count(char) != t.count(char):
                return char
        return ""