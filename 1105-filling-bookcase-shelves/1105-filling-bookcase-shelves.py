class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  
        
        for i in range(1, n+1):
            width = 0
            maxHeigth = 0
            j = i
            while j > 0:
                width += books[j - 1][0]
                if width > shelfWidth:
                    break
                maxHeigth = max(maxHeigth, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + maxHeigth)
                j -= 1
        
        return dp[n]
       