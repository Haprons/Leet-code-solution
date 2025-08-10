class Solution {
    public boolean doesAliceWin(String s) {
        int count = 0;
        int n = s.length();

        for(int i = 0 ; i < n ; i++){
            if(s.charAt(i) == 'a' || s.charAt(i) == 'e' || s.charAt(i) == 'i' || s.charAt(i) == 'o' || s.charAt(i) == 'u' )
                count++;
        }
        
        return count > 0;
    }
}