class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
            else:
                count += 1
        
        for i in  range(len(nums)):
            if count > 1:
                nums[i] = 0
            elif count == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else :
                nums[i] = product//nums[i]  
        return nums
