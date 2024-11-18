class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        if k == 0:
            return result
        
        if k > 0:
            for i in range(n):
                for j in range(1, k+1):
                    idx = (i + j) % n
                    result[i] += code[idx]
        
        if k < 0:
            for i in range(n):
                for j in range(-1, k-1, -1):
                    idx = (i + j + n) % n
                    result[i] += code[idx]
        
        return result
