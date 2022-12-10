class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0
        
        while i < len(slots1) and j < len(slots2):
            a, b = slots1[i]
            c, d = slots2[j]

            if c > b:
                i += 1
            elif a > d:
                j += 1
            else:
                start = max(a, c)
                end = min(b, d)
                if end - start >= duration:
                    return [start, start + duration]
                else:
                    if d > b:
                        i += 1
                    elif b > d:
                        j += 1
                    else:
                        i += 1
                        j += 1
        
        return []

solution = Solution()
assert solution.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15],[60, 70]], 8) == [60, 68]
assert solution.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12) == []