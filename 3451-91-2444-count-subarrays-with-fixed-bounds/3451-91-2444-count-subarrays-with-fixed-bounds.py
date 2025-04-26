class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left_bound = -1
        last_minK = -1
        last_maxK = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i
            
            if num == minK:
                last_minK = i
            
            if num == maxK:
                last_maxK = i
            
            valid_start = min(last_minK, last_maxK)
            if valid_start > left_bound:
                count += valid_start - left_bound
                
        
        return count
        