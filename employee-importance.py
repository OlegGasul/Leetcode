from collections import defaultdict

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id: int) -> int:
        graph = defaultdict(set)

        for emp in employees:
            graph[emp.id] = [emp.importance, emp.subordinates]

        result = 0
        visited = set()

        def dfs(id):
            nonlocal result
            nonlocal visited

            importance, subordinates = graph[id]
            result += importance
            visited.add(id)

            for sub in subordinates:
                if sub in visited:
                    continue
                
                dfs(sub)

        dfs(id)

        return result

solution = Solution()
print(solution.getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1))