import functools

class Solution:
    def earliestFullBloom(self, plantTime, growTime) -> int:
        zipped = zip(plantTime, growTime)
        
        def compare(a, b):
            return b[1] - a[1]
        
        zipped = sorted(zipped, key = functools.cmp_to_key(compare))

        result = 0
        time = 0
        
        for plant, grow in zipped:
            time += plant

            result = max(result, time + grow)
            
            
        return result

solution = Solution()
print(solution.earliestFullBloom([1, 4, 3], [2, 3, 1]))
print(solution.earliestFullBloom([1, 2, 3, 2], [2, 1, 2, 1]))