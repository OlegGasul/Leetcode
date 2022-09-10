from collections import defaultdict
from collections import Counter

def minimumTime(n: int, relations, time) -> int:
    graph = defaultdict(set)
    degrees = Counter()

    def getZeroDegrees():
        mostCommon = degrees.most_common()
        if not mostCommon:
            return []
        
        result = []

        while mostCommon and mostCommon[-1][1] == 0:
            node = mostCommon[-1][0]
            result.append(node)
            
            mostCommon.pop(-1)
            del degrees[node]

        return result


    for edge in range(1, n + 1):
        degrees[edge] = 0

    for relation in relations:
        graph[relation[0]].add(relation[1])
        degrees[relation[1]] += 1

    result = 0

    queue = getZeroDegrees()

    while queue:
        maximum = float('-inf')
        for node in queue:
            maximum = max(maximum, time[node - 1])
            
            for edge in graph[node]:
                degrees[edge] -= 1

        result += maximum
        queue = getZeroDegrees()

    
    return result

print(minimumTime(9, [[2, 7], [2, 6], [3, 6], [4, 6], [7, 6], [2, 1], [3, 1], [4, 1], [6, 1], [7, 1], [3, 8], [5, 8], [7, 8], [1, 9], [2, 9], [6, 9], [7, 9]], [9, 5, 9, 5, 8, 7, 7, 8, 4]))
print(minimumTime(1, [], [1]))
print(minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]))
print(minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]))