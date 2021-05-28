import heapq


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = {}

        for u in range(n):
            graph[u] = []

        for u,v,w in flights:
            graph[u].append((v,w))

        heap = [(0,-K,src)]

        while heap:
            (cost,i,u) = heapq.heappop(heap)

            if u == dst:
                return cost

            for v,w in graph[u]:
                nc = cost + w

                if i <= 0:
                    heapq.heappush(heap, (nc,i+1,v))

        return -1