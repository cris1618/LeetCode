int chalkReplacer(int* chalk, int chalkSize, int k) {
        long long int total_chalk = 0;
        for(int i = 0; i<chalkSize; i++){
            total_chalk += chalk[i];
        }
        k = k % total_chalk;
        
        
        int index = 0;
        while(1){
            if (k < chalk[index]){
                return index;
            }
            k -= chalk[index];
            index = (index + 1) % chalkSize;
        }
            
        
        return index;
}