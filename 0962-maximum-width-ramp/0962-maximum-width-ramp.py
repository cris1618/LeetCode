class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indicies = [i for i in range(n)]
        
        indicies.sort(key=lambda i: (nums[i], i))
        
        min_index = n
        max_width = 0
        
        for i in indicies:
            max_width = max(max_width, i-min_index)
            min_index = min(min_index, i)
        
        return max_width
                    
        