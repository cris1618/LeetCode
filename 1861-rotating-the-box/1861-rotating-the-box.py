class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # Simulate gravity for each row
        for row in box:
            empty = len(row) - 1  # Start from the bottom of the row
            for col in range(len(row) - 1, -1, -1):
                if row[col] == '#':
                    row[col], row[empty] = row[empty], row[col]  # Move stone down
                    empty -= 1  # Update the next empty spot
                elif row[col] == '*':
                    empty = col - 1  # Obstacle blocks further movement

        # Rotate the box 90 degrees clockwise
        rotated = [[box[row][col] for row in range(len(box) - 1, -1, -1)] for col in range(len(box[0]))]

        return rotated