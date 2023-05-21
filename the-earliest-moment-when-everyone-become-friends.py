class Solution:
    def earliestAcq(self, logs, n: int) -> int:
        logs.sort()

        parent = [i for i in range(n)]
        
        def findParent(id):
            if parent[id] == id:
                return id
            return findParent(parent[id])
        
        def union(a, b):
            parent[a] = b

        for time, a, b in logs:
            x = findParent(a)
            y = findParent(b)
            if x != y:
                union(x, y)

                n -= 1
                if n == 1:
                    return time
        
        return -1

solution = Solution()
assert solution.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6) == 20190301
assert solution.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4) == 3