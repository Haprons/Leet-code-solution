class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.count_nums = {}
        for num in nums2 :
            if num not in self.count_nums : 
                self.count_nums[num] = 0 
            self.count_nums[num] += 1 
        print(self.count_nums)
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.count_nums[self.nums2[index]] -= 1 
        self.nums2[index] += val 
        if self.nums2[index] not in self.count_nums : 
            self.count_nums[self.nums2[index]] = 0 
        self.count_nums[self.nums2[index]] += 1 
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        total = 0 
        for num in self.nums1 :
            if tot-num in self.count_nums : 
                total += self.count_nums[tot-num]
        return total


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)