class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        min_val = arrays[0][0]  
        max_val = arrays[0][-1]  
        max_diff = 0  
        
        for i in range(1, n):
            max_diff = max(max_diff, abs(arrays[i][-1] - min_val))
            
            max_diff = max(max_diff, abs(max_val - arrays[i][0]))
            
            
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return max_diff
         
        
       
    
                
                
        