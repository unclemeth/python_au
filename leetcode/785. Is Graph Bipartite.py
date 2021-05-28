import collections


class Solution:
    def isBipartite(self, graph):
        n,color = len(graph), {}
        for i in range(n):
            if i not in color and graph[i]:
                color[i] = 1
                Q = collections.deque([i])
                while Q:
                    u = Q.popleft()
                    for v in graph[u]:
                        if v not in color:
                            color[v] = 1 - color[u]
                            Q.append(v)
                        elif color[v] == color[u]:
                            return False
        return True