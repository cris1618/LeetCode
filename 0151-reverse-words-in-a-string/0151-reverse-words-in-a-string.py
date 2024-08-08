class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)
        
        reversed_words = []
        
        for i in range(n - 1, -1, -1):
            reversed_words.append(words[i])
        
            
        return " ".join(reversed_words)
            
            
       
        
        