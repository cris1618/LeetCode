class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total_chalk = sum(chalk)
        k = k % total_chalk
        
        
        index = 0
        while True:
            if k < chalk[index]:
                return index
            k -= chalk[index]
            index = (index + 1) % n
        
        return index