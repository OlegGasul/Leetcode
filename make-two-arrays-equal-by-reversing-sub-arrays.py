def canBeEqual(target, arr) -> bool:
    if len(target) != len(arr):
        return False
        
    target.sort()
    arr.sort()
        
    for i in range(len(target)):
        if target[i] != arr[i]:
            return False
            
    return True

print(canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
print(canBeEqual([3, 7, 9], [3, 7, 11]))