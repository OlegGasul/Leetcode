def findOrder(numCourses: int, prerequisites):
    prereq = { c: [] for c in range(numCourses) }

    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    result = []
    visited, cycle = set(), set()

    print(prereq)

    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visited:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False
            
        cycle.remove(crs)
        visited.add(crs)
        result.append(crs)
        
        return True

    for c in range(numCourses):
        if not dfs(c):
            return []

    return result

print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2], [0, 2]]))
