class Solution {
public:
    vector<int> grayCode(int n) {
        int N=pow(2,n);
        vector<int> gray(N);
        for(int i=0;i<N;i++){
            gray[i]=(i^(i>>1));
        }

        return gray;

    }
};