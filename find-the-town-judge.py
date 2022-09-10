from collections import Counter
from collections import defaultdict

def findJudge(n: int, trust) -> int:
    if len(trust) == 0 and n > 1:
        return -1
        
    if len(trust) == 0 and n == 1:
        return 1
        
    trustCounter = Counter()
    graph = defaultdict(set)
        
    for t in trust:
        graph[t[0]].add(t[1])
        trustCounter[t[1]] += 1
                
    mostCommon = trustCounter.most_common()[0]
    if mostCommon[1] < n - 1 or len(graph[mostCommon[0]]) > 0:
        return -1
        
    return mostCommon[0]

print(findJudge(3, [[1, 2], [2, 3]]))
print(findJudge(3, [[1, 3], [2, 3]]))