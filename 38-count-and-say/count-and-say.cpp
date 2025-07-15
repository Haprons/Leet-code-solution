class Solution {
public:
    string countAndSay(int n) {
      string result = "1";
      for(int i = 1; i < n ; i++ ){
        result = expand(result);
      }
      return result;
    }
private:
    string expand(const string& s){
        string res = "";
        int count = 1;
        for(int i = 1; i < s.size();i++){
            if (s[i] == s[i-1])
                count++;
            else{
                res += to_string(count) + s[i-1];
                count = 1;
            }
        }
        res += to_string(count) + s.back();
        return res;
    }
};