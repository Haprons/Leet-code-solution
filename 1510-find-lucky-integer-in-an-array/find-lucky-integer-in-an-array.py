class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maxe = 0
        for num in arr[::-1]:
            if num == arr.count(num):
                maxe = max(num,maxe)
        if maxe != 0:
            return maxe
        return -1