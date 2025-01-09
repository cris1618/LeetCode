class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(words)
        count = 0

        for i in range(n):
            if words[i].startswith(pref):
                count += 1
        
        return count
        