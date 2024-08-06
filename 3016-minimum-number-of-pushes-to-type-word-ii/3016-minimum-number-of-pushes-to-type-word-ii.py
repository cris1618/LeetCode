from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        sorted_freq = sorted(freq.values(), reverse=True)
        n = len(sorted_freq)
        
        
        num_keys = 8
        total_presses = 0
        press_cost = 1
        
        for i in range(n):
            key_press_number = i // num_keys + 1
            total_presses += sorted_freq[i] * key_press_number
        
        return total_presses