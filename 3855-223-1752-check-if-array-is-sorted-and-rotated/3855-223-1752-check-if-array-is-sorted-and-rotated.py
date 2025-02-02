class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_arr = sorted(nums)
        
        if sorted_arr == nums:
            return True
        
        for rotation_offset in range(n):
            is_match = True
            for index in range(n):
                if nums[(rotation_offset + index) % n] != sorted_arr[index]:
                    is_match = False
                    break
            if is_match:
                return True
        
        return False
        

        