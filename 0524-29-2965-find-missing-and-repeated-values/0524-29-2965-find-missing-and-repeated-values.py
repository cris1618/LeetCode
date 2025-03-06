class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [0, 0]
        n = len(grid)
        bool_list = [False]*n**2  
       
        for i in range(n):
            for j in range(n):
                if bool_list[grid[i][j] - 1] == True:
                    arr[0] = grid[i][j]
                else:
                    bool_list[grid[i][j] - 1] = True
        
        num_missing = bool_list.index(False) + 1
        arr[1] = num_missing

        return arr
        
        