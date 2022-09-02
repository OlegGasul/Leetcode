import heapq

def maximumProduct(nums) -> int:
    largest = heapq.nlargest(3, nums)
    smallest = heapq.nsmallest(2,nums)

    return max(largest[0] * largest[1] * largest[2], largest[0] * smallest[0] * smallest[1])

print(maximumProduct([1, 2, 3]))
print(maximumProduct([1, 2, 3, 4]))
print(maximumProduct([-1, -2, -3]))
print(maximumProduct([1, -2, -3, 0, 0]))