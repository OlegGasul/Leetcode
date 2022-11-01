from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes):
        groups = defaultdict(list)
        
        for i in range(len(groupSizes)):
            groups[groupSizes[i]].append(i)
            
        result = []
        
        for size, people in groups.items():
            i = 0
            while i < len(people):
                result.append(people[i : i + size])
                i += size
                
        return result

solution = Solution()
print(solution.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(solution.groupThePeople([2, 1, 3, 3, 3, 2]))