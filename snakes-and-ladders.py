import math
import heapq

class Solution:
    def snakesAndLadders(self, board) -> int:
        if board[0][0] != -1:
            return -1
        
        n = len(board)
        n2 = n ** 2
        
        def cellByNumber(pos):
            row = n - math.ceil(pos / n)
            col = pos % n
            if (n - row - 1) % 2 == 0:
                if col == 0:
                    col = n - 1
                else:
                    col -= 1
            elif col != 0:
                col = n - col

            return row, col

        result = float('inf')
        visited = {}

        hp = []
        heapq.heappush(hp, (-1, 0))
        visited[1] = 0

        while hp:
            pos, steps = heapq.heappop(hp)
            
            pos = -pos
            if pos == n2:
                result = min(result, steps)
                continue
            
            last = min(pos + 6, n2)
            
            for p in range(pos + 1, last + 1):
                i, j = cellByNumber(p)
                
                newPos = board[i][j]
                if newPos > 0:
                    if not newPos in visited or visited[newPos] > steps + 1:
                        visited[newPos] = steps + 1
                        heapq.heappush(hp, (-newPos, steps + 1))
                else:
                    if not p in visited or visited[p] > steps + 1:
                        visited[p] = steps + 1
                        heapq.heappush(hp, (-p, steps + 1))

        return result

solution = Solution()
assert solution.snakesAndLadders([[-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 35, -1, -1, 13, -1],
    [-1, -1, -1, -1, -1, -1],
    [-1, 15, -1, -1, -1, -1]]) == 4

assert solution.snakesAndLadders([[1, 1, -1],
    [1, 1, 1],
    [-1, 1, 1]]) == -1