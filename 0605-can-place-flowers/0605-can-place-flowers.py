class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        m = len(flowerbed)
        
        for i in range(m):
            if flowerbed[i] == 0:
                prev = (i == 0) or (flowerbed[i - 1] == 0)
                next = (i == m - 1) or (flowerbed[i + 1] == 0)
                
                if prev and next:
                    flowerbed[i] = 1
                    count += 1
            
            if count >= n:
                return True
        
        return False
            
        