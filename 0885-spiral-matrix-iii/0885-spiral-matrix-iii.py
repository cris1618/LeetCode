class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        total_cells = rows * cols
        steps = 1
        direction = 0
        r, c = rStart, cStart
         
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while len(result) < total_cells:
            for _ in range(2):
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                    r += directions[direction][0]
                    c += directions[direction][1]
                direction = (direction + 1) % 4
            steps += 1
            
        return result
                
                
        