class Solution:
    def reverseWords(self, s: str) -> str:
        words = ["".join(reversed(word)) for word in s.split()]
        return " ".join(words)