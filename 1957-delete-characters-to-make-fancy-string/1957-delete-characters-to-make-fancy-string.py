class Solution:
    def makeFancyString(self, s: str) -> str:
        count_rep = 1
        n = len(s)
        ans = s[0]
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                count_rep += 1
            else:
                count_rep = 1
                
            if count_rep < 3:
                ans += s[i]
                    
                
        return ans
            
        