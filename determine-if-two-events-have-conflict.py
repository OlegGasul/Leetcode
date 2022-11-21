import functools

class Solution:
    def haveConflict(self, event1, event2) -> bool:
        def timeToMins(val):
            return int(val[:2]) * 60 + int(val[3:])

        a, b = timeToMins(event1[0]), timeToMins(event1[1])
        c, d = timeToMins(event2[0]), timeToMins(event2[1])

        totalDay = 60 * 24

        ranges = []
        if a > b:
            ranges.append([b, totalDay])
            ranges.append([0, a])
        else:
            ranges.append([a, b])

        if c > d:
            ranges.append([d, totalDay])
            ranges.append([0, c])
        else:
            ranges.append([c, d])

        def compare(a, b):
            return a[1] - b[1] if a[0] == b[0] else a[0] - b[0]

        ranges = sorted(ranges, key = functools.cmp_to_key(compare))

        for i in range(1, len(ranges)):
            a, b = ranges[i - 1]
            c, d = ranges[i]

            if c <= b:
                return True

        return False

solution = Solution()
print(solution.haveConflict(["10:00", "11:00"], ["14:00", "15:00"]))
print(solution.haveConflict(["01:15", "02:00"], ["02:00", "03:00"]))