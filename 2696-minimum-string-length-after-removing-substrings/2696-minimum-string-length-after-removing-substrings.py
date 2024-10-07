class Solution:
    def minLength(self, s: str) -> int:
        n = len(s)
        i = 0
        while i < n-1:
            if s[i:i+2] == 'AB' or s[i:i+2] == 'CD':
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        
        """for i in range(n-1):
            if s[i:i+2] == 'AB' or s[i:i+2]:
                s = s[:i] + s[i+2:]
                i -= 1
            else:
                i += 1"""
                
        return len(s)