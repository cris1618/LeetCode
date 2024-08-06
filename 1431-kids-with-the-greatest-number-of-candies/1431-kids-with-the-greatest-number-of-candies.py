class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = []
        max_can = max(candies)
        
        
        for i in range(n):
            if candies[i] + extraCandies >= max_can:
                result.append(True)
            else:
                result.append(False)
        
        return result
            
        
        