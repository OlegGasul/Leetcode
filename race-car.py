from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set([(0, 1)])

        while queue:
            position, speed, steps = queue.popleft()

            if position == target:
                return steps

            if (position + speed, 2 * speed) not in visited:
                queue.append((position + speed, 2 * speed, steps + 1))
                visited.add((position + speed, 2 * speed))

            if speed > 0 and (position, -1) not in visited:
                queue.append((position, -1, steps + 1))
                visited.add((position, -1))
            elif speed <= 0 and (position, 1) not in visited:
                queue.append((position, 1, steps + 1))
                visited.add((position, 1))

solution = Solution()
assert solution.racecar(3) == 2
assert solution.racecar(6) == 5