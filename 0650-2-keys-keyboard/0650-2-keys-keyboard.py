class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        
        operations = 0
        
        f = 2
        while f*f <= n:
            while n%f == 0:
                operations += f
                n //= f
            f+=1
        
        if n>1:
            operations += n
                
        return operations
                
            
            
            
            
        
        