class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        pos = 0
        
        
        while pos < len(word):
            consecutive_count = 0
            
            current_char = word[pos]
            while(pos < len(word) and consecutive_count < 9 and word[pos] == current_char):
                consecutive_count += 1
                pos += 1
            
            comp += str(consecutive_count) + current_char
            
        return comp
            
            
                
            
            
            
        