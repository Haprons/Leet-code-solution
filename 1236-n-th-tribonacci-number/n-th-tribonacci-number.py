class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0) : return 0
        if(n == 1) or (n==2) : return 1
        t1,t2,t3 = 0,1,1
        for _ in range(n-2):
            sum = t1 + t2 + t3
            t1,t2,t3 = t2,t3,sum
        return t3

        