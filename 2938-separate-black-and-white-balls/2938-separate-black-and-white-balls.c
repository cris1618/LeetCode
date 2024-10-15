#include <string.h>

long long minimumSteps(char* s) {
    int n = strlen(s);  
    int whiteSpace = 0;
    long long totalSwaps = 0;
    
    for(int currentPos = 0; currentPos<n; currentPos++){
        if(s[currentPos] == '0'){
            totalSwaps += currentPos - whiteSpace;
            whiteSpace++;
        }
    }
    return totalSwaps;
}