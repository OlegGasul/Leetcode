def minMoves(nums) -> int:
    minimum = float('inf')
    result = 0
        
    for n in nums:
        result += n
        minimum = min(minimum, n)
            
    return result - len(nums) * minimum

print(minMoves([1, 2, 3]))
print(minMoves([1, 1, 1]))