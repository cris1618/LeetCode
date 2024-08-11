class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def isDisconnected(grid):
            def dfs(r, c):
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 1:
                    return
                grid[r][c] = -1  #mark as visited
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(r + dr, c + dc)
            
            num_islands = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        if num_islands > 0:
                            return True  
                        num_islands += 1
                        dfs(i, j)
            
            return num_islands != 1
        
        
        if isDisconnected([row[:] for row in grid]):
            return 0
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if isDisconnected([row[:] for row in grid]):
                        return 1
                    grid[i][j] = 1  
        
        
        return 2
                