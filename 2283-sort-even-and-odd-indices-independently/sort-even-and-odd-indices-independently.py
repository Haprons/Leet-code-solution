class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = sorted([nums[i] for i in range(len(nums)) if i % 2 == 0])
        b = sorted([nums[i] for i in range(len(nums)) if i % 2 != 0],reverse = True)
        even , odd = 0 , 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = a[even]
                even += 1
            else:
                nums[i] = b[odd]
                odd += 1
        return nums
