class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        n_pairs = len(nums) // 2
        used_element = [False] * n
        number_of_pairs = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] == nums[j] 
                    and used_element[i] == False 
                    and used_element[j] == False):
                        number_of_pairs += 1
                        used_element[i] = True
                        used_element[j] = True
        
        return number_of_pairs == n_pairs



        