# Hint 3
# Let arr2XorSum = (arr2[0]^arr2[1]^arr2[2]...), arr1XorSum = (arr1[0]^arr1[1]^arr1[2]...)
# so the final answer is (arr2XorSum&arr1[0]) ^ (arr2XorSum&arr1[1]) ^ (arr2XorSum&arr1[2]) ^ ... = arr2XorSum & arr1XorSum.

def getXORSum(arr1, arr2) -> int:
    arr1XorSum = arr1[0]
    for i in range(1, len(arr1)):
        arr1XorSum ^= arr1[i]
            
    arr2XorSum = arr2[0]
    for i in range(1, len(arr2)):
        arr2XorSum ^= arr2[i]
            
    return arr1XorSum & arr2XorSum

print(getXORSum([1, 2, 3], [6, 5]))
print(getXORSum([12], [4]))