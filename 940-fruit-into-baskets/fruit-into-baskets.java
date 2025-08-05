class Solution {
    public int totalFruit(int[] fruits) {
        int last = -1 , second_last = -1 , curr = 0 , last_count = 0 , res = 0 ;
        for (int f : fruits){
            if (f == last || f == second_last)
            {
                curr += 1;
            }
            else
            {
                curr = last_count + 1;
            }
            if (f == last)
            {
                last_count += 1;
            }
            else
            {
                last_count = 1;
                second_last = last;
                last = f;
            }
            res = Math.max(res,curr);
        }
        return res;
    }
}