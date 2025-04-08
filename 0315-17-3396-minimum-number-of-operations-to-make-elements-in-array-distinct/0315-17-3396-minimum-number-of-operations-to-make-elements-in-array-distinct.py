class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        total_op = 0
        

        while(i < n):
            if len(set(nums)) == len(nums):
                return total_op
            else:
                nums = nums[i+3:]
                total_op += 1
        
        return total_op



        