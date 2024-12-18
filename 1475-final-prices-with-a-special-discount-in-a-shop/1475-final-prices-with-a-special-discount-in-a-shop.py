class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = [0] * n
        
        for i in range(1, n+1):
            for j in range(1, n):
                if(j > i-1 and prices[j] <= prices[i-1]):
                    answer[i-1] = prices[i-1] - prices[j]
                    print(prices[i-1], prices[j])
                    break
                else:
                    answer[i-1] = prices[i-1]
        
        return answer
        