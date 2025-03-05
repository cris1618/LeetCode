class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        colored = 1
        for i in range(1, n):
            colored = colored + (4*i)
        
        return colored


        