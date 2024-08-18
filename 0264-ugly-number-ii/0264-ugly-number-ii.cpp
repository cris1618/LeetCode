using namespace std;
#include <vector>
#include <algorithm>
class Solution {
public:
    int nthUglyNumber(int n) {
        vector <int> ugly_numbers(n);
        ugly_numbers[0] = 1;
        
       
        int i2 = 0;
        int i3 = 0;
        int i5 = 0;
        
       
        int next_multiple_of_2 = 2;
        int next_multiple_of_3 = 3;
        int next_multiple_of_5 = 5;
        
        for(int i = 1; i<n; ++i){
            int next_ugly = min(next_multiple_of_2, min(next_multiple_of_3, next_multiple_of_5));
            ugly_numbers[i] = next_ugly;
            
            
            if(next_ugly == next_multiple_of_2){
                 i2 += 1;
                next_multiple_of_2 = ugly_numbers[i2] * 2;
            }
               
            
            if(next_ugly == next_multiple_of_3){
                i3 += 1;
                next_multiple_of_3 = ugly_numbers[i3] * 3;
            }
                
            
            if(next_ugly == next_multiple_of_5){
                i5 += 1;
                next_multiple_of_5 = ugly_numbers[i5] * 5;
            }
                
        }
            
        
        
        return ugly_numbers[n-1];
    }
};