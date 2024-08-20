class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        dp = [[0] * (n + 1) for _ in range(n)]

        def helper(i, m):
            if i == n:
                return 0
            
            if 2 * m >= n - i:
                return suffix_sum[i]
            
            if dp[i][m] != 0:
                return dp[i][m]

            max_stones = 0
            for x in range(1, 2 * m + 1):
                max_stones = max(max_stones, suffix_sum[i] - helper(i + x, max(m, x)))

            dp[i][m] = max_stones
            return dp[i][m]

        return helper(0, 1)

        
        
            