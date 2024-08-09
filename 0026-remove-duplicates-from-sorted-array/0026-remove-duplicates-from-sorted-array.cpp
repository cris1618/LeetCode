class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) {
    return 0;
}
        
        int n = nums.size();
        int unique_index = 0;
        
        for(int i = 1; i<n; ++i){
            if(nums[i] != nums[unique_index]){
                 unique_index += 1;
                nums[unique_index] = nums[i];
            }
               
        }
            
        
        return unique_index + 1;
    }
};