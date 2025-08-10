import java.util.*;
class Solution {
    public int countPermutations(int[] complexityplexity) {
        if (complexityplexity.length <= 1) {
            return 1;
        }
        
        int first = complexityplexity[0];
        for (int i = 1; i < complexityplexity.length; i++) {
            if (complexityplexity[i] <= first) {
                return 0;
            }
        }
        
        long ans = 1;
        int mod = 1_000_000_007;
        int n = complexityplexity.length;
        
        for (int j = 1; j < n; j++) {
            ans = (ans * j) % mod;
        }
        
        return (int) ans;
    }
}