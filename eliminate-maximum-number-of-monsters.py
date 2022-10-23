from cgitb import reset
import math

def eliminateMaximum(dist, speed) -> int:
    length = len(dist)
    dp = [1 if speed[i] >= dist[i] else math.ceil(1.0 * dist[i] / speed[i]) for i in range(length)]
    dp.sort()
    
    for i in range(length):
        if dp[i] < i + 1:
            return i

    return length


print(eliminateMaximum([3, 2, 4], [5, 3, 2]))
print(eliminateMaximum([1, 3, 4], [1, 1, 1]))