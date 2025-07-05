from math import log
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        res = round(log(n,3))
        return 3**res == n