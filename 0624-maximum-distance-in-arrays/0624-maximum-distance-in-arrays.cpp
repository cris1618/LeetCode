#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>  

using namespace std;

class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        int n = arrays.size();
        int min_val = arrays[0][0];  
        int max_val = arrays[0].back();  
        int max_diff = 0;
        
        for(int i = 1; i < n; ++i) {
            max_diff = max(max_diff, arrays[i].back() - min_val);
        
            max_diff = max(max_diff, max_val - arrays[i][0]);
            
            
            min_val = min(min_val, arrays[i][0]);
            max_val = max(max_val, arrays[i].back());
        }
        
        return max_diff;
    }
};