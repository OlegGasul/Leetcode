class Solution:
    def maxDistToClosest(self, seats) -> int:
        zeros = 0
        isFirst = True
        hasOne = False
        result = 0
        
        for s in seats:
            if s == 1:
                hasOne = True
                if isFirst:
                    result = zeros
                    isFirst = False
                else:
                    if zeros % 2 == 1:
                        zeros += 1
                    result = max(result, zeros // 2)
                zeros = 0
            else:
                zeros += 1

        if not hasOne:
            return len(seats)

        return max(result, zeros)

solution = Solution()
print(solution.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
print(solution.maxDistToClosest([1, 0, 1, 0, 0, 0, 0]))
print(solution.maxDistToClosest([1, 0, 0, 0]))
print(solution.maxDistToClosest([1, 0]))
print(solution.maxDistToClosest([0, 1]))
print(solution.maxDistToClosest([1, 1]))
print(solution.maxDistToClosest([0, 0]))