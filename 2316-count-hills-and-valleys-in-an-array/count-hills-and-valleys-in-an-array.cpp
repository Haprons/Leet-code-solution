class Solution {
public:
    int countHillValley(vector<int>& nums) {
        int n = nums.size();
        int diff[2] = {0,0};
        int count = 0 , i = 0;
        int prev = nums[0];
        int bigger;
        while (i < n){
            while (i < n && prev == nums[i])
                i++;
            if ( i == n )
                break;
            if ( nums[i] > prev )
                bigger = 1;
            else
                bigger = 0;
            diff[bigger] = 1;
            count += diff[bigger] && diff[1-bigger];
            diff[1 - bigger] = 0;
            prev = nums[i];
            i++;
        }
        return count;
    }
};