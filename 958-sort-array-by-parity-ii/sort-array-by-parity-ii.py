class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        i ,j = 0 , 1
        for h in range(len(nums)):
            if nums[h] % 2 == 0 :
                ans[i] = nums[h]
                i += 2
            else:
                ans[j] = nums[h]
                j += 2
        return ans
