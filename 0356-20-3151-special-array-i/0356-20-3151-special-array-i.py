class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True

        for i in range(1, n):
            if (
                ((nums[i-1] % 2 == 0) and (nums[i] %2 != 0)) 
                or ((nums[i-1] % 2 != 0) and (nums[i] % 2 == 0))
            ):
                continue
            else:
                print(nums[i-1], nums[i])
                return False

        return True  