class Solution {
    public int maximumProduct(int[] nums) {
        int first= Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        int third = Integer.MIN_VALUE;
        int min1 = 0;
        int min2=0;
        
        for(int num: nums) {
            if(num>third) {
                if(num>first) {
                    third = second;
                    second = first;
                    first = num;
                } else 
                    if(num > second) {
                        third = second;
                        second = num;
                    } else {
                        third = num;
                    }
                
            }
            if(num <min2) {
                if(num <min1) {
                    min2 = min1;
                    min1 = num;
                } else {
                    min2 =num;
                }
            }
        }
        return Math.max(first*second*third, first*min1*min2);
    }
}