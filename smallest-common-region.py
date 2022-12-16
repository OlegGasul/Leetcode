from collections import defaultdict

class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        if region1 == region2:
            return region1
        
        parent = defaultdict(str)

        for i in range(len(regions)):
            p = regions[i][0]

            for j in range(1, len(regions[i])):
                parent[regions[i][j]] = p

        visited = set()

        a = region1
        b = region2
        
        visited.add(a)
        visited.add(b)

        while a or b:
            a = parent[a]
            b = parent[b]

            if not a and not b:
                return ""
            
            if a:
                if a in visited:
                    return a
                else:
                    visited.add(a)
            
            if b:
                if b in visited:
                    return b
                else:
                    visited.add(b)
        
        return ""

solution = Solution()
assert solution.findSmallestRegion([["Earth","North America","South America"],
    ["North America","United States","Canada"],
    ["United States","New York","Boston"],
    ["Canada","Ontario","Quebec"],
    ["South America","Brazil"]], "Quebec", "New York") == "North America"