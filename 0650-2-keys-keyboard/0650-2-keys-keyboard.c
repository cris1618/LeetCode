int minSteps(int n) {
    if(n == 1){
            return 0;
         }
            
        
        int operations = 0;
        
        int f = 2;
        while(f*f <= n){
            while(n%f == 0){
               operations += f;
                n /= f;
            }
                
            f+=1;
        }
            
        
        if(n>1){
           operations += n; 
        }
            
                
        return operations;
        
    }
