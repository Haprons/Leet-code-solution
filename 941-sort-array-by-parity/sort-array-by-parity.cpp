class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        int left = 0 , right = nums.size()- 1;
        int temp;
        while (left < right) {
            if (nums[left] % 2 == 0)
                left ++;
            else {
                temp = nums[left] ;
                nums[left] = nums[right];
                nums[right] = temp;
                right --;
            }
        }
        return nums;
    }
};