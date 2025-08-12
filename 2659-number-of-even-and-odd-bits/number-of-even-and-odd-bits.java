class Solution {
    public int[] evenOddBit(int n) {
        String s = Integer.toBinaryString(n);
        int[] res = new int[2];       
        // Traverse from right to left (LSB to MSB)
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(s.length() - 1 - i); // reverse index
            if (ch == '1') {
                res[i % 2]++; // i%2==0 => even bit, i%2==1 => odd bit
            }
        }        
        return res;
    }
}