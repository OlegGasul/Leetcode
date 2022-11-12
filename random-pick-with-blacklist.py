class Solution:

    def __init__(self, n: int, blacklist):
        self.n = n
        self.ranges = []
        self.index = 0

        def insertIntoRanges(n):
            left = 0
            right = len(self.ranges) - 1

            while left <= right:
                middle = left + (right - left) // 2
                a, b = self.ranges[middle]
                if n >= a and n <= b:
                    return

                if n - 1 == b:
                    self.ranges[middle][1] = n
                    if middle + 1 < len(self.ranges):
                        a1, b1 = self.ranges[middle + 1]
                        if n + 1 == a1:
                            self.ranges[middle] = [a, b1]
                            self.ranges.pop(middle + 1)
                        else:
                            self.ranges[middle] = [a, n]
                    else:
                        self.ranges[middle] = [a, n]

                    return

                if n + 1 == a:
                    self.ranges[middle][0] = n
                    if middle - 1 >= 0:
                        a1, b1 = self.ranges[middle - 1]
                        if n - 1 == b1:
                            self.ranges[middle] = [a1, b]
                            self.ranges.pop(middle - 1)
                        else:
                            self.ranges[middle] = [n, b]
                    else:
                        self.ranges[middle] = [n, b]

                    return

                if n > b:
                    left = middle + 1
                elif n < a:
                    right = middle - 1
            
            self.ranges.insert(left, [n, n])

        for n in blacklist:
            if not self.ranges:
                self.ranges.append([n, n])
                continue

            insertIntoRanges(n)

        if self.ranges:
            self.ranges.append([self.n, float('inf')])
        
        self.current = -1

        self.allBanned = self.ranges and (self.ranges[0][0] <= 0 and self.ranges[0][1] >= self.n - 1)
        

    def pick(self) -> int:
        if self.allBanned:
            return -1
        
        self.current += 1
        if self.current >= self.n:
            self.current = 0
            self.index = 0

        if not self.ranges:
            return self.current
        
        a, b = self.ranges[self.index]
        while self.current >= a:
            self.current = b + 1
            
            if self.current >= self.n:
                self.current = 0
                self.index = 0
            else:
                self.index += 1
            
            a, b = self.ranges[self.index]

        return self.current
        

solution = Solution(7, [2, 3, 5])
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())
print(solution.pick())

solution = Solution(3, [0, 1, 2])
print(solution.pick())
print(solution.pick())

solution = Solution(3, [2])
print(solution.pick())
print(solution.pick())
print(solution.pick())
