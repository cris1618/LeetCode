import heapq
from typing import List


class Solution:
    INF = int(2e9)

    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        # Step 1: Compute the initial shortest distance from source to destination
        current_shortest_distance = self.run_dijkstra(
            edges, n, source, destination
        )

        # If the current shortest distance is less than the target, return an empty result
        if current_shortest_distance < target:
            return []
        matches_target = current_shortest_distance == target

        # Step 2: Iterate through each edge to adjust its weight if necessary
        for edge in edges:
            # Skip edges that already have a positive weight
            if edge[2] > 0:
                continue

            # Set edge weight to a large value if current distance matches target, else set to 1
            edge[2] = self.INF if matches_target else 1

            # Step 3: If current shortest distance does not match target
            if not matches_target:
                # Compute the new shortest distance with the updated edge weight
                new_distance = self.run_dijkstra(edges, n, source, destination)
                # If the new distance is within the target range, update edge weight to match target
                if new_distance <= target:
                    matches_target = True
                    edge[2] += target - new_distance

        # Return modified edges if the target distance is achieved, otherwise return an empty result
        return edges if matches_target else []


    def run_dijkstra(self, edges: List[List[int]], n: int, source: int, destination: int) -> int:
        adj_matrix = [[] for _ in range(n)]
        for nodeA, nodeB, weight in edges:
            if weight != -1:
                adj_matrix[nodeA].append((nodeB, weight))
                adj_matrix[nodeB].append((nodeA, weight))

        min_distance = [self.INF] * n
        min_distance[source] = 0
        pq = [(0, source)]  # (distance, node)

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > min_distance[u]:
                continue

            for v, weight in adj_matrix[u]:
                distance = current_dist + weight
                if distance < min_distance[v]:
                    min_distance[v] = distance
                    heapq.heappush(pq, (distance, v))

        return min_distance[destination]
