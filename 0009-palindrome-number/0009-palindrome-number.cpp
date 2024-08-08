#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
         string num_str = to_string(x);
        
        
        int left = 0;
        int right = num_str.size() - 1;
        
       
        
        while(left < right){
            if(num_str[left] != num_str[right]){
                return false;
            }
                
            left += 1;
            right -= 1;
        }
            
        
        return true;
    }
};