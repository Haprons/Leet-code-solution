class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        a = sorted(nums)
        count = 0
        for k in range(2,len(nums)):
            num = a[k]
            i , j = 0 , k - 1
            while i < j:
                if a[i] + a[j] > num:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count