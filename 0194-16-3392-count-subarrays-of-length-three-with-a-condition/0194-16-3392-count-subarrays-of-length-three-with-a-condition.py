class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        num_sub = 0
        for i in range(n):
            for j in range(i+2, n):
                if (nums[i] + nums[j] == nums[j-1]/2) and len(nums[i:j+1]) == 3:
                    num_sub += 1
                    continue
        
        return num_sub
                
        