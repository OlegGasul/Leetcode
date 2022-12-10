class Solution:
    def minAvailableDuration(self, slots1, slots2, duration: int):
        slots1.sort(reverse = True)
        slots2.sort(reverse = True)
        
        while slots1 and slots2:
            a, b = slots1[-1]
            c, d = slots2[-1]

            if c > b:
                slots1.pop()
            elif a > d:
                slots2.pop()
            else:
                start = max(a, c)
                end = min(b, d)
                if end - start >= duration:
                    return [start, start + duration]
                else:
                    if d > b:
                        slots1.pop()
                    elif b > d:
                        slots2.pop()
                    else:
                        slots1.pop()
                        slots2.pop()
        
        return []

solution = Solution()
assert solution.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15],[60, 70]], 8) == [60, 68]
assert solution.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12) == []