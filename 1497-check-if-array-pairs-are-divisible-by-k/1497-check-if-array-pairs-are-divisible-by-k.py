class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) == 0:
            return False
        if k == 0:
            return False
        
        remainders = [0]*k
        
        for num in arr:
            remainder = num % k
            remainders[remainder] += 1
        
        for i in range(1, k):
            if remainders[i] != remainders[k-i]:
                return False
        
        if remainders[0] % 2 != 0:
            return False
        
        return True
                    
        