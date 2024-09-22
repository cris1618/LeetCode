int min(int x,int y){
    if(x<y)
        return x;
    else
        return y;
}

int count_steps(long long n,long long prefix1, long long prefix2){
     int steps = 0;
        while(prefix1 <= n){
            steps += min(n+1, prefix2) - prefix1;
            prefix1 *= 10;
            prefix2 *= 10;
        
        }
        return steps;    
}
       

int findKthNumber(int n, int k) {
    int curr = 1;
    k -= 1;
        
    while(k > 0){
        int step = count_steps(n, curr, curr + 1);
            if(step <= k){
                curr += 1;
                k -= step;
            }else{
                curr *= 10;
                k -= 1;
            }   
    }
    return curr;
}