import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        stack = []
        cnt = 0
        inDeg = [0]*numCourses
        print(inDeg)
        for node in prerequisites:
            graph[node[1]].add(node[0])
            inDeg[node[0]]+=1
        for i in range(numCourses):
            if inDeg[i] == 0:
                stack.append(i)
        while stack:
            next_n = stack.pop()
            for i in graph[next_n]:
                inDeg[i]-=1
                if inDeg[i] == 0:
                    stack.append(i)
            cnt+=1
        return cnt == numCourses