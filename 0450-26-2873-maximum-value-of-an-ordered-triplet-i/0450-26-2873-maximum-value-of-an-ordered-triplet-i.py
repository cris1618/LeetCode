class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = 0

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    current_triplet = (nums[i] - nums[j]) * nums[k]
                    max_val = max(max_val, current_triplet)
        
        return max_val

        