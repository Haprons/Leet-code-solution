class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(),players.end());
        sort(trainers.begin(),trainers.end());
        int res = 0;
        int i = 0;
        int p = players.size();
        int t = trainers.size();
        for(int j = 0 ; j < t ; j++){
            if(players[i] <= trainers[j]){
                res++;
                i++;
                if(i == p)
                    break;
            }
        }
        return res;
    }
};