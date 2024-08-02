class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        merge = ""
        
        i = 0
        while i < n1 or i < n2:
            if i < n1:
                merge += word1[i]
            if i < n2:
                merge += word2[i]
            i += 1
            
                
        return merge
        