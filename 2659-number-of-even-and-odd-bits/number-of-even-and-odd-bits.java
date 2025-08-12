class Solution {
    public int[] evenOddBit(int n) {
        int arr[] = new int[2];

        int even=0;
        int odd=0;
        int pos=0;
        while(n!=0)
        {
            int a = (n&1);
            if(a==1)
            {
                if(pos%2==0)
                even++;
                else
                odd++;

            }
            pos++;
            n>>=1;
        }
        arr[0]=even;
        arr[1]=odd;
        return arr;
    }
}