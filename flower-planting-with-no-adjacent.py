from collections import defaultdict

def gardenNoAdj(n: int, paths):
    graph = defaultdict(set)
        
    colors = set([1, 2, 3, 4])
        
    result = [0] * n
        
    for u, v in paths:
        graph[u].add(v)
        graph[v].add(u)
            
    for i in range(1, n + 1):
        choosenColors = set()
        for v in graph[i]:
            if result[v - 1] > 0:
                choosenColors.add(result[v - 1])
                    
        result[i - 1] = (colors - choosenColors).pop()
            
    return result

print(gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]))
print(gardenNoAdj(4, [[1, 2], [3, 4]]))
print(gardenNoAdj(4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))