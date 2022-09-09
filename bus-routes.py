import collections

def numBusesToDestination(routes, source: int, target: int) -> int:
    if source == target:
        return 0
    
    routes = [set(x) for x in routes]
    graph = collections.defaultdict(set)
    
    for i, r1 in enumerate(routes):
        for j in range(i + 1, len(routes)):
            r2 = routes[j]
            if any(r in r2 for r in r1):
                graph[i].add(j)
                graph[j].add(i)

    print(routes)

    for key, value in graph.items():
        print(key, value)

    seen, targets = set(), set()
    for node, route in enumerate(routes):
        if source in route:
            seen.add(node)
        if target in route:
            targets.add(node)

    queue = [(node, 1) for node in seen]
    for node, depth in queue:
        if node in targets: return depth
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                queue.append((nei, depth + 1))
    
    return -1

print(numBusesToDestination([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12))
print(numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))