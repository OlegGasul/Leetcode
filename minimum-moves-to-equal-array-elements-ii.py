def minMoves2(nums) -> int:
    middle = sorted(nums)[len(nums) // 2]
    result = 0
    
    for n in nums:
        result += abs(n - middle)
            
    return result

print(minMoves2([0, 0, 1, 6, 8]))
print(minMoves2([1, 8, 6]))