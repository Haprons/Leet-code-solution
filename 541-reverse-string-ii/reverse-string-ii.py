class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 0
        while i < len(s):
            s[i:k+i] = reversed(s[i:k+i])
            i += 2 * k
        return "".join(s)