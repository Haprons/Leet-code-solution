class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int count = 0;
        for(int k = 2 , n = nums.size() ; k < n ; k++){
            int num = nums[k] , i = 0 , j = k - 1;
            while(i < j){
                if (nums[i] + nums[j] > nums[k]){
                    count += j - i;
                    --j;
                }
                else ++i;
            }
        }
        return count;
    }
};