class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        comm_server = 0
        num_server = 0
        n_row = len(grid)
        n_col = len(grid[0]) if n_row > 0 else 0
        
        # Check for row servers
        for row in range(n_row):
            for col in range(n_col):
                if grid[row][col] == 1:
                    can_communicate = False

                    for other_col in range(n_col):
                        if other_col != col and grid[row][other_col] == 1:
                            can_communicate = True
                            break
                    
                    if can_communicate: 
                        comm_server += 1
                    else:
                        for other_row in range(n_row):
                            if other_row != row and grid [other_row][col] == 1:
                                can_communicate = True
                                break
                        
                        if can_communicate:
                            comm_server += 1
        
        return comm_server


        