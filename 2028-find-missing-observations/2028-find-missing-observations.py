class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        
        sum_m = sum(rolls)
        m_avg = sum_m/m
        remaining_sum = mean*(n + m) - sum_m
        
        max_sum = n * 6
        min_sum = n
        
        if remaining_sum > max_sum or remaining_sum < min_sum:
            return []
        
        distribute_mean = remaining_sum//n
        mod = remaining_sum % n
        
        new_list = [distribute_mean] * n
        for i in range(mod):
            new_list[i] += 1
        
        return new_list
            
        
        
            
            
        