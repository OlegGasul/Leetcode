from collections import deque

class Solution:
    def getFood(self, grid) -> int:
        def isValid(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 'X'
        
        def getPosition():
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '*':
                        return (i, j)
        i, j = getPosition()
        
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        queue = deque()
        queue.append((i, j, 0))
        seen = {(i, j)}
        
        while queue:
            i, j, steps = queue.popleft()
            if grid[i][j] == '#':
                return steps
            
            for dx, dy in directions:
                newI, newJ = i + dx, j + dy
                if (newI, newJ) not in seen and isValid(newI, newJ):
                    seen.add((newI, newJ))
                    queue.append((newI, newJ, steps + 1))
                    
        return -1

            
solution = Solution()

print(solution.getFood([
    ["X","X","X","X","X","X"],
    ["X","*","O","O","O","X"],
    ["X","O","O","#","O","X"],
    ["X","X","X","X","X","X"]]))

print(solution.getFood([
    ["X","X","X","X","X"],
    ["X","*","X","O","X"],
    ["X","O","X","#","X"],
    ["X","X","X","X","X"]]))

print(solution.getFood([
    ["X","X","X","X","X","X","X","X"],
    ["X","*","O","X","O","#","O","X"],
    ["X","O","O","X","O","O","X","X"],
    ["X","O","O","O","O","#","O","X"],
    ["X","X","X","X","X","X","X","X"]]))