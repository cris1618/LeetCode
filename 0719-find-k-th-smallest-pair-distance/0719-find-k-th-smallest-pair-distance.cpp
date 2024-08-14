using namespace std;
#include <vector>
#include <bits/stdc++.h> 
#include <algorithm>

int countPairs(int mid, vector<int> nums){
    int count = 0;
    int left = 0;
    int n = nums.size();
    for(int right = 0; right < n; ++right){
         while(nums[right] - nums[left] > mid){
             left += 1;
             
         }
                            
            count += right - left;            
    
            
    }
     return count;          
}
            

class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        
        
        
        int low = 0;
        int high = nums.back() - nums[0]; 
        
        while(low < high){
            int mid = (low + high) / 2;
            if(countPairs(mid, nums) < k){
                low = mid + 1;
            }
            else{
                high = mid;
            }
        }
            
        
        return low;
    }
};