class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        i = 0
        for num in nums:
            if num % 2 == 0 :
                ans[i] = num
                i += 2
        i = 1
        for num in nums:
            if num % 2 != 0 :
                ans[i] = num
                i += 2
        return ans
