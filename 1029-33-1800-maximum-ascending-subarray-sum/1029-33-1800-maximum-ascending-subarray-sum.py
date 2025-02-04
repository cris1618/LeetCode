class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        max_sub = 0
        
        for i in range(n):
            max_temp = nums[i]
            for j in range(i+1, n):
                if nums[j-1] < nums[j]:
                    max_temp += nums[j] 
                else:
                    break
            
            max_sub = max(max_sub, max_temp)
        
        return max_sub
            

        