class Solution {
public:
    static bool comp(vector<int>&a,vector<int>&b)
    {
        return a[1] < b[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),comp);
        int cet = INT_MIN ,res = 0;
        for(auto i : intervals)
        {
            if(i[0] >= cet)
                cet = i[1];
            else
                ++res;
        }
        return res;
    }
};