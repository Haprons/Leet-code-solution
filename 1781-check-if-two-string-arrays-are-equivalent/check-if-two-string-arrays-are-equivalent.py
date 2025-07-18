class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordstr1 = "".join(word1)
        wordstr2 = "".join(word2)
        if wordstr1 == wordstr2:
            return True
        return False