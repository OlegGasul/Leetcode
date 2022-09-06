def maxWidthRamp(nums) -> int:
    dp = [(a, i) for i, a in enumerate(nums)]
    dp.sort()

    print(dp)

    minimumIndex = float('Inf')
    result = 0
    
    # We need to find maximum index difference
    for value, i in dp:
        result = max(result, i - minimumIndex)
        minimumIndex = min(minimumIndex, i)

    return result

print(maxWidthRamp([6, 0, 8, 2, 1, 5]))