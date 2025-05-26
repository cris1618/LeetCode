class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        g = [[] for _ in range(n)]
        in_deg = [0]*n
        for u,v in edges:
            g[u].append(v)
            in_deg[v] += 1
        
        # dp[u][c] = max count of color c up to and including u
        dp = [[0]*26 for _ in range(n)]
        q = deque([i for i in range(n) if in_deg[i] == 0])
        visited = 0

        while q:
            u = q.popleft()
            visited += 1

            col_idx = ord(colors[u]) - ord("a")
            dp[u][col_idx] += 1

            for v in g[u]:
                for c in range(26):
                    if dp[u][c] > dp[v][c]:
                        dp[v][c] = dp[u][c]
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
        
        if visited < n:
            return -1
        
        return max(max(row) for row in dp)
