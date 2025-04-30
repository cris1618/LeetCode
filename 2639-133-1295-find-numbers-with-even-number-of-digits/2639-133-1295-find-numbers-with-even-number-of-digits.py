class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        even_count = 0
        for i in range(n):
            str_num = str(nums[i])
            len_dig = len(str_num)
            if len_dig % 2 == 0:
                even_count += 1
            else:
                continue
        
        return even_count

        
        