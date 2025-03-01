class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
            else:
                continue
        
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        
        return nums


        