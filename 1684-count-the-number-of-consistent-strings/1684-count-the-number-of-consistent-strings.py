class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        for word in words: 
            is_word_consistent = True
            for char in word:
                is_char_allowed = False
                for allowed_char in allowed:
                    if allowed_char == char:
                        is_char_allowed = True
                        break
                    
                if not is_char_allowed:
                    is_word_consistent = False
                    break
                
            if is_word_consistent:
                count += 1
                
        return count
                
        