class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for k in range(2,len(nums)):
            num = nums[k]
            i , j = 0 , k - 1
            while i < j:
                if nums[i] + nums[j] > num:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count