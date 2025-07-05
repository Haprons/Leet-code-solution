class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        sum_divisor = 1  # start with 1, since 1 is always a divisor
        i = 2
        while i * i <= num:
            if num % i == 0:
                sum_divisor += i
                if i != num // i:
                    sum_divisor += num // i
            i += 1
        
        return sum_divisor == num
