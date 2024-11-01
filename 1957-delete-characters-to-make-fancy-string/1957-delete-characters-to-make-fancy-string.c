#define MAX_STRING 100000

char* makeFancyString(char* s) {
    char* ans = malloc(MAX_STRING);
    if(!ans) return NULL;
    int count_rep = 1;
    int n = strlen(s);
    int pos = 0;
    
    ans[pos++] = s[0];
    
        
        for(int i = 1; i<n; i++){
            if(s[i] == s[i-1])
                count_rep += 1;
            else
                count_rep = 1;
                
            if(count_rep <  3)
                ans[pos++] = s[i];
        }
    
    ans[pos] = '\0';
            
                    
                
        return ans;
}