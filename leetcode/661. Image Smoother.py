class Solution:
    def imageSmoother(self, M):
        def a(M,i,j):
            ans = 0
            p = [i-1,i,i+1]
            q = [j-1,j,j+1]
            if -1 in p:
                p.pop(0)
            if len(M) in p:
                p.pop()
            if -1 in q:
                q.pop(0)
            if len(M[0]) in q:
                q.pop()
            c = 0
            for a in p:
                for b in q:
                    ans += M[a][b]
                    c += 1
            return ans//c
        N = []
        for i in range(len(M)):
            temp = []
            for j in range(len(M[0])):
                temp.append(a(M,i,j))
            N.append(temp)
        return N