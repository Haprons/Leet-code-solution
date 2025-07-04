int fib(int n){
    if(n == 0|| n == 1 ) return n;
    int a = 0,b= 1;
    int sum;
    for(int i=2;i< n + 1;i++ ){
        sum = a + b;
        a = b;
        b = sum;
    }
    return sum;
}