#include <algorithm>
using namespace std;

class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        n = nums.size();
        
        vector<int> subarray_sums;
        for(int i = 0; i<n; ++i){
            int current_sum = 0;
            for(int j = i; j<n; ++j){
                current_sum += nums[j];
                subarray_sums.push_back(current_sum); 
            }                
        }
        
        sort(subarray_sums.begin(), subarray_sums.end());
        
        long long result = 0;
        int MOD = 1e9 + 7; 

        for (int i = left - 1; i < right; ++i) {
            result = (result + subarray_sums[i]) % MOD;
}
                
        return result;
    }
};