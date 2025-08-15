class Solution {
public:
    vector<int> grayCode(int n) {
        vector<string> a, tmp = {"0","1"};
        vector<int> res;
        for(int i = 2; i <= n;i++){
            a = tmp;
            tmp.clear();
            for(string s : a) tmp.push_back('0' + s);
            reverse(a.begin(),a.end());
            for(string s : a) tmp.push_back('1' + s);
        }
        for (string s : tmp) res.push_back(stoi(s,nullptr,2));
        return res;
    }
};