from collections import defaultdict

class Solution:
    def findAllPeople(self, n: int, meetings, firstPerson: int):
        meetMap = {}

        for a, b, t in meetings:
            if not t in meetMap:
                meetMap[t] = defaultdict(set)
            
            meetMap[t][a].add(b)
            meetMap[t][b].add(a)

        withSecret = set([0, firstPerson])

        def dfs(graph, node, visited):
            if node in visited:
                return
            visited.add(node)

            for v in graph[node]:
                if v in visited:
                    continue
                dfs(graph, v, visited)

        for t in sorted(meetMap.keys()):
            graph = meetMap[t]
            
            visited = set()
            for p in set(graph.keys()).intersection(withSecret):
                if p in visited:
                    continue
                
                dfs(graph, p, visited)

            withSecret.update(visited)


        return list(withSecret)

solution = Solution()
print(solution.findAllPeople(6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1))
print(solution.findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3))
print(solution.findAllPeople(5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 3))