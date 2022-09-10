from collections import defaultdict

def checkIfPrerequisite(numCourses: int, prerequisites, queries):
    graph = defaultdict(set)
        
    for prerequisite in prerequisites:
        graph[prerequisite[0]].add(prerequisite[1])
            
    def search(node, target, visited):
        visited.add(node)
            
        for edge in graph[node]:
            if edge in visited:
                continue
            if edge == target:
                return True
                
            if search(edge, target, visited):
                return True
                
        return False
        
    result = []
        
    for query in queries:
        result.append(search(query[0], query[1], set()))
            
    return result

print(checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
print(checkIfPrerequisite(2, [], [[1, 0], [0, 1]]))
print(checkIfPrerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]))