class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = 0
        if(len(s) == 0 ): return True
        if(len(t) == 0 ): return False
        for x in t:
            if count < len(s) and s[count] == x:
                count += 1
        return count == len(s)