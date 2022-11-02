class Solution:
    def minimumCost(self, cost) -> int:
        cost.sort()
        
        result = 0
        
        while cost:
            if len(cost) >= 3:
                result += cost.pop()
                result += cost.pop()
                cost.pop()
            else:
                result += sum(cost)
                return result
            
        return result

solution = Solution()
print(solution.minimumCost([1, 2, 3]))
print(solution.minimumCost([6, 5, 7, 9, 2, 2]))
print(solution.minimumCost([2, 2]))
print(solution.minimumCost([]))