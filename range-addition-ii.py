def maxCount(m: int, n: int, ops) -> int:
    if len(ops) == 0:
        return m * n
    
    minA = float("inf")
    minB = float("inf")
    
    for op in ops:
        minA = min(op[0], minA)
        minB = min(op[1], minB)

    return minA * minB

print(maxCount(3, 3, [[2, 2], [3, 3]]))
print(maxCount(10, 10, [[2, 2], [3, 3], [4, 4]]))
print(maxCount(3, 3, []))