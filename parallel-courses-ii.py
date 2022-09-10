from collections import defaultdict
import math

def minNumberOfSemesters(n: int, relations, k: int) -> int:
    degrees = [0] * (n + 1)

    edges = defaultdict(set)

    for relation in relations:
        edges[relation[0]].add(relation[1])
        degrees[relation[1]] += 1

    queue = []

    for i in range(1, n + 1):
        if degrees[i] == 0:
            queue.append(i)

    result = 0
    courses = k
    visited = set()

    while queue:
        result += math.ceil(len(queue) / k)
        
        for course in queue:
            visited.add(course)

        newQueue = []

        for node in queue:
            degrees[node] -= 1
            
            for edge in edges[node]:
                if edge in visited:
                    continue

                degrees[edge] -= 1

                if degrees[edge] == 0:
                    newQueue.append(edge)

        queue = newQueue

    return result

print(minNumberOfSemesters(13, [[12, 8], [2, 4], [3, 7], [6, 8], [11, 8], [9, 4], [9, 7], [12, 4], [11, 4], [6, 4], [1, 4], [10, 7], [10, 4], [1, 7], [1, 8], [2, 7], [8, 4], [10, 8], [12, 7], [5, 4], [3, 4], [11, 7], [7, 4], [13, 4], [9, 8], [13, 8]], 9))
print(minNumberOfSemesters(5, [[1, 5], [1, 3], [1, 2], [4, 2], [4, 5], [2, 5], [1, 4], [4, 3], [3, 5], [3, 2]], 3))
print(minNumberOfSemesters(11, [], 2))
print(minNumberOfSemesters(4, [[2, 1], [3, 1], [1, 4]], 2))
print(minNumberOfSemesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2))