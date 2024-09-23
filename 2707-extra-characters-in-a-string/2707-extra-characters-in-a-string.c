#include <stdio.h>
#include <string.h>
#include <limits.h>

int IsInDictionary(char **dictionary, int dictionarySize, char *substring){
    for(int i = 0; i < dictionarySize; i++){
        if(strcmp(dictionary[i], substring) == 0){
            return 1;
        }
    }
    return 0;
}

int minExtraChar(char * s, char ** dictionary, int dictionarySize){
    int n = strlen(s);
    int dp[n+1];
    
    for(int i = 0; i<=n; i++){
        dp[i] = 0;
    }
    
    for(int start = n -1; start>=0; start--){
        dp[start] = dp[start + 1] + 1;
        
        for(int end = start; end < n; end++){
            char curr[end-start+2];
            strncpy(curr, s+start, end-start+1);
            curr[end - start + 1] = '\0';
            if(IsInDictionary(dictionary, dictionarySize, curr)){
                dp[start] = (dp[start] < dp[end+1]) ? dp[start] : dp[end+1];
            }
        }
    }
return dp[0];
}