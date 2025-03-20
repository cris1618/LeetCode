class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        
        visited = [False] * n

        components = [0] * n
        components_cost = []

        component_id = 0

        for node in range(n):
            if not visited[node]:
                components_cost.append(
                    self._get_component_cost(
                        node, adj_list, visited, components, component_id
                    )
                )
                component_id += 1
        
        result = []
        for query in query:
            start, end = query
            if components[start] == components[end]:
                result.append(components_cost[components[start]])
            else:
                result.append(-1)
        
        return result
    
    def _get_component_cost(
        self, source, adj_list, visited, components, component_id
    ):
        nodes_queue = deque()

        components_cost = -1
        nodes_queue.append(source)
        visited[source] = True

        while nodes_queue:
            node = nodes_queue.popleft()
            components[node] = component_id
            for neighbor, weight in adj_list[node]:
                components_cost &= weight

                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                nodes_queue.append(neighbor)
        
        return components_cost

        