class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        
        dp = points[0]
        
        for i in range(1, n):
            left_max = [0] * m
            right_max = [0] * m
            
            left_max[0] = dp[0]
            for j in range(1, m):
                left_max[j] = max(left_max[j - 1] - 1, dp[j])
            
            right_max[m - 1] = dp[m - 1]
            for j in range(m - 2, -1, -1):
                right_max[j] = max(right_max[j + 1] - 1, dp[j])
            
            for j in range(m):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])
        
        return max(dp)
        
        
        
        
            