class Solution {
public:
    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        int k = 0;
        
        
        for(int num : nums) {
            k += num;
        }
        
        
        if(k == 0 || k == n) {
            return 0;
        }
        
        
        vector<int> extended(n * 2);
        for(int i = 0; i < n; ++i) {
            extended[i] = nums[i];
            extended[i + n] = nums[i]; 
        }
        
        int zero_count = 0;
        
       
        for(int i = 0; i < k; ++i) {
            if(extended[i] == 0) {
                zero_count += 1;
            }
        }
        
        int min_swaps = zero_count;
        
        
        for(int i = 1; i < n; ++i) {
            if(extended[i - 1] == 0) {
                zero_count -= 1;
            }
            if(extended[i + k - 1] == 0) {
                zero_count += 1;
            }
            
            min_swaps = std::min(min_swaps, zero_count);
        }
        
        return min_swaps;
    }
};