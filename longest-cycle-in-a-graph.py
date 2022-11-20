class Solution:
    def longestCycle(self, edges) -> int:
        longest = -1
        visited = {}

        def dfs(node, curr):
            while True:
                if node in visited:
                    return curr - visited[node]
                visited[node] = curr
            
                if edges[node] < 0:
                    return -1
                
                nextNode = edges[node]
                edges[node] = -1
                node = nextNode
                curr += 1
                    
        for i in range(len(edges)):
            if edges[i] != -1:
                visited = {}
                longest = max(dfs(i, 0), longest)
        
        return longest

solution = Solution()
assert solution.longestCycle([3, 3, 4, 2, 3]) == 3
assert solution.longestCycle([2, -1, 3, 1]) == -1