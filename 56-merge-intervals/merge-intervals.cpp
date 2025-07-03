class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>>res;
        int currIdx = -1;
        for (auto interval : intervals) {
            if (res.empty() || interval[0] > res[currIdx][1]) {
                // non-merged case
                res.push_back(interval);
                ++currIdx;
            } else // merged case
            {
                res[currIdx][1] = max(res[currIdx][1], interval[1]);
            }
        }
        return res;
    }
};