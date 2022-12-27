class Solution:
    def canReach(self, arr, start: int) -> bool:
        n = len(arr)
        visited = set()

        def dfs(index):
            if index < 0 or index >= n:
                return False
            
            if index in visited:
                return False
            
            if arr[index] == 0:
                return True
            
            value = arr[index]
            visited.add(index)

            if dfs(index + value):
                return True
            
            if dfs(index - value):
                return True
            
            return False
        
        return dfs(start)

solution = Solution()
assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 5) == True
assert solution.canReach([4, 2, 3, 0, 3, 1, 2], 0) == True
assert solution.canReach([3, 0, 2, 1, 2], 2) == False