def canMakeArithmeticProgression(arr) -> bool:
    length = len(arr)
    if length <= 2:
        return True
    
    arr = sorted(arr)
    diff = arr[1] - arr[0]

    for i in range(2, length):
        if arr[i] - arr[i - 1] != diff:
            return False
    
    return True


print(canMakeArithmeticProgression([3, 5, 1]))
print(canMakeArithmeticProgression([1, 2, 4]))