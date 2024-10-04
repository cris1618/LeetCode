class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        n_2 = int(n / 2)
        skill.sort()
        pairs = []
        products = []
    
        for i in range(n_2):
            pairs.append((skill[i], skill[n - 1 - i]))
        
        target_sum = skill[0] + skill[-1]
        
        for k, v in pairs:
            if k + v == target_sum:
                products.append(k * v)
            else:
                return -1
            
        return sum(products)

            
            