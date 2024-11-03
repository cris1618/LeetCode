class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        new_string = ""
        
        if s == goal:
            return True
        
        for i in range(1, n):
            new_string = s[i:n] + s[0:i]
            if(new_string==goal):
                return True
            
        
        return False
             
        