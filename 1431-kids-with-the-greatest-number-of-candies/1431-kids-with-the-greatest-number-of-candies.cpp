using namespace std;
#include <vector>

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        vector<bool> result;
        int max_can = *max_element(candies.begin(), candies.end());
        
        
        for(int i = 0; i<n; ++i){
            if(candies[i] + extraCandies >= max_can){
                result.push_back(true);
            }
        
            else{
                result.push_back(false);
            }
        }
            
                
        
        return result;
    }
};