class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])
        
        def is_magic_square(grid, start_row, start_col):
            nums = set()
            sums = []

            # Check all numbers from 1 to 9 are present
            for i in range(3):
                for j in range(3):
                    num = grid[start_row + i][start_col + j]
                    if num < 1 or num > 9:  # Only numbers 1-9 are valid
                        return False
                    nums.add(num)

            if len(nums) != 9:
                return False

            # Check row sums
            for i in range(3):
                row_sum = sum(grid[start_row + i][start_col + j] for j in range(3))
                sums.append(row_sum)

            # Check column sums
            for j in range(3):
                col_sum = sum(grid[start_row + i][start_col + j] for i in range(3))
                sums.append(col_sum)

            # Check diagonal sums
            diag1_sum = grid[start_row][start_col] + grid[start_row + 1][start_col + 1] +                     grid[start_row + 2][start_col + 2]
            diag2_sum = grid[start_row][start_col + 2] + grid[start_row + 1][start_col + 1] +                 grid[start_row + 2][start_col]

            sums.append(diag1_sum)
            sums.append(diag2_sum)

            # All sums must be equal
            return all(s == sums[0] for s in sums)
        
        count = 0   
        for i in range(0, nrow - 2):
            for j in range(0, ncol - 2):
                if is_magic_square(grid, i, j):
                    count += 1
        
        return count
                    
                
        
        