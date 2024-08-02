class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        k = sum(nums)
        
        if k == 0 or k == n:
            return 0
        
        extended = nums + nums
        zero_count = 0
        
        for i in range(k):
            if extended[i] == 0:
                zero_count += 1
        
        min_swaps = zero_count
        
        for i in range(1, n):
            if extended[i - 1] == 0:
                zero_count -= 1
            if extended[i + k - 1] == 0:
                zero_count += 1
            
            min_swaps = min(min_swaps, zero_count)
        
        return min_swaps
                
        