class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degree = [0]*n
        
        
        for i in range(len(edges)):
            in_degree[edges[i][1]] += 1
            
        champ = -1
        champ_count = 0
        
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                champ_count += 1
                champ = i
        
        return champ if champ_count == 1 else -1
            