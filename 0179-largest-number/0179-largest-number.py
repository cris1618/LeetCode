class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(x) for x in nums]
        nums.sort(key=lambda a: a*10, reverse=True)
        
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)
        