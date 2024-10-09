class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)
        min_adds_required = 0
        count_open = 0
        
        for i in range(n):
            if s[i] == '(':
                count_open += 1
            else:
                if count_open > 0:
                    count_open -= 1
                else:
                    min_adds_required += 1
        
        return min_adds_required + count_open