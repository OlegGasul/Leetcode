from collections import deque

class Solution:
    def nearestExit(self, maze, entrance) -> int:
        rows = len(maze)
        cols = len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r, c = entrance
        maze[r][c] = '+'

        queue = deque()
        queue.append([r, c, 0])
        
        while queue:
            r, c, dist = queue.popleft()

            for d in directions:
                r1 = r + d[0]
                c1 = c + d[1]

                if 0 <= r1 < rows and 0 <= c1 < cols and maze[r1][c1] == '.':
                    if r1 == 0 or r1 == rows - 1 or c1 == 0 or c1 == cols - 1:
                        return dist + 1

                    maze[r1][c1] = '+'
                    queue.append([r1, c1, dist + 1])

        return -1
                
solution = Solution()
print(solution.nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))
print(solution.nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))