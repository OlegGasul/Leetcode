import bisect

class Solution:
    def fullBloomFlowers(self, flowers, persons):
        starts = []
        ends = []

        for i in range(len(flowers)):
            starts.append(flowers[i][0])
            ends.append(flowers[i][1])

        starts.sort()
        ends.sort()

        result = [0] * len(persons)

        for i in range(len(persons)):
            result[i] = bisect.bisect_right(starts, persons[i]) - bisect.bisect_left(ends, persons[i])

        return result

solution = Solution()
print(solution.fullBloomFlowers([[1, 6], [3, 7], [9, 12], [4, 13]], [2, 3, 7, 11]))
print(solution.fullBloomFlowers([[1, 10], [3, 3]], [3, 3, 2]))
        