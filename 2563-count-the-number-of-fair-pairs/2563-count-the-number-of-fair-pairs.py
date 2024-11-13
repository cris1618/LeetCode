class Solution:
    def lower_bounds(self,nums, low, high, element):
        while low <= high:
            mid = low + ((high - low) // 2)
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            low = self.lower_bounds(nums, i+1, len(nums) - 1, lower - nums[i])
            high = self.lower_bounds(nums, i+1, len(nums) - 1, upper - nums[i] + 1)
            
            ans += high - low
        
        return ans
        
                
        
        