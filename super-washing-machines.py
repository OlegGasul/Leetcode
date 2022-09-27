def findMinMoves(machines) -> int:
    total, length = sum(machines), len(machines)
    if total % length:
        return -1
    
    target, result, toRight = total // length, 0, 0
    
    for machine in machines:
        toRight = machine + toRight - target
        result = max(result, abs(toRight), machine - target)
    
    return result
    
print(findMinMoves([4, 0, 0, 4]))
print(findMinMoves([1, 0, 5]))
print(findMinMoves([0, 3, 0]))
print(findMinMoves([0, 0, 0, 7, 0, 0, 0]))
print(findMinMoves([0, 2, 0]))