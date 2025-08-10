class Solution {
    public boolean reorderedPowerOf2(int n) {
        String s = count(n);
        for (int i = 0; i < 31; i++)
            if (s.equals(count(1 << i))) return true;
        return false;
    }
    private String count(int x) {
        int[] cnt = new int[10];
        while (x > 0) { cnt[x % 10]++; x /= 10; }
        StringBuilder sb = new StringBuilder();
        for (int c : cnt) sb.append(c);
        return sb.toString();
    }
}