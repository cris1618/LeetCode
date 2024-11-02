class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        n = len(s)
        print(n)
        
        if n == 1:
            if(s[0][0] == s[0][-1]):
                return True
            
            
        for i in range(1, n):
            if(s[i-1][-1] != s[i][0]):
                return False
            
        return s[0][0] == s[-1][-1]      
        