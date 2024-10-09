#include <string.h>

int minAddToMakeValid(char* s) {
    int openBrackets = 0;
        int minAddsRequired = 0;
        int size = strlen(s);
        for(int i = 0; i<size; i++){
            if(s[i] == '('){
                openBrackets++;
            }else{
                openBrackets > 0 ? openBrackets-- : minAddsRequired++;
            }
        }
        return openBrackets + minAddsRequired;
}