class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        check_string1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        check_string2 = check_string1.lower()
        word1 = word[0]
        word2 = word[1:]
        if all(char in check_string1 for char in word):
            return True
        elif all(char in check_string2 for char in word):
            return True
        elif all(char in check_string2 for char in word2) and word1 in check_string1:
            return True
        return False