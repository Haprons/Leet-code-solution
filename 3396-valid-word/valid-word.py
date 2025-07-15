class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        v,c =0,0
        for i in word:
            if i.isalpha():
                if i in 'aeiouAEIOU':
                    v += 1
                else:
                    c += 1
            elif i.isalnum():
                pass
            else:
                return False
        if v > 0 and c >0:
            return True
        return False