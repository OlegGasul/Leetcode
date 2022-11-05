class Solution:
    def numberOfWeakCharacters(self, properties) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        stack = []
        result = 0
        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                result += 1
            
            stack.append(d)
        
        return result
        
solution = Solution()
print(solution.numberOfWeakCharacters([[7, 7], [1, 2], [9, 7], [7, 3], [3, 10], [9, 8], [8, 10], [4, 3], [1, 5], [1, 5]]))
