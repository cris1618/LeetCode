class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg = 0
        count_pos = 0

        for i in range(len(nums)):
            if nums[i] < 0 and nums[i] != 0:
                count_neg += 1
            elif nums[i] > 0 and nums[i] != 0:
                count_pos += 1
        
        return max(count_neg, count_pos)
        