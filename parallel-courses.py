class Solution:
    def minimumSemesters(self, n: int, relations) -> int:
        graph = {i: set() for i in range(1, n + 1)}
        for u, v in relations:
            graph[u].add(v)

        distances = {}

        def dfs(node):
            if node in distances:
                return distances[node]
            
            distances[node] = -1

            result = 1
            for v in graph[node]:
                length = dfs(v)
                
                if length == -1:
                    return -1
                else:
                    result = max(result, length + 1)
            
            distances[node] = result
            
            return result

        result = -1
        for node in graph.keys():
            length = dfs(node)
            if length == -1:
                return -1
            
            result = max(length, result)
        
        return result

solution = Solution()
assert solution.minimumSemesters(3, [[1, 3], [2, 3]]) == 2
assert solution.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]) == -1