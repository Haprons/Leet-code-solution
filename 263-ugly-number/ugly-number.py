class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        
        for i in [2,3,5]:
            while n % i == 0:
                n = n // i

        return n == 1
        