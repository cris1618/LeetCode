class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        result = 0
        
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0] = floor(gifts[0] ** (1/2))
        
        for j in range(len(gifts)):
            result += gifts[j]
            
        return result
        