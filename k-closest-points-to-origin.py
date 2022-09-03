import functools
import math

def kClosest(points, k: int):
    for i in range(len(points)):
        points[i].append(math.sqrt(points[i][0] ** 2 + points[i][1] ** 2))
            
    def compare(a, b):
        return a[2] - b[2]
        
    points = sorted(points, key = functools.cmp_to_key(compare))
        
    result = []
    for i in range(k):
        result.append([points[i][0], points[i][1]])
            
    return result

print(kClosest([[1, 3], [-2, 2]], 1))
print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))