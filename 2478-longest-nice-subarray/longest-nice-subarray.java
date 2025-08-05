class Solution {
    public int longestNiceSubarray(int[] nums) {
        int n = nums.length;
        int res = 1;
        int left = 0;
        int bitmask = 0;

        for (int right = 0; right < n; right++) {
            // Remove conflict from the window
            while ((bitmask & nums[right]) != 0) {
                bitmask ^= nums[left]; // remove leftmost number
                left++;
            }

            bitmask |= nums[right]; // include current number
            res = Math.max(res, right - left + 1);
        }

        return res;
    }
}
