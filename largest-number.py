import functools

def largestNumber(nums) -> str:
    if len(nums) == 0:
        return ""
    
    if len(nums) == 1:
        return str(nums[0])
    
    if all(x == 0 for x in nums):
        return "0"

    nums = map(lambda x: str(x), nums)

    def compare(n, m):
        if n + m > m + n:
            return -1
        else:
            return 1

    return ''.join(sorted(nums, key = functools.cmp_to_key(compare)))

# ['9', '5', '34', '30', '3']
# 9 5 34 3 30
print(largestNumber([3, 30, 34, 5, 9]))
print(largestNumber([0, 0]))
print(largestNumber([0, 1]))

# Output
# "9077746056515513321"
# "9077746056551513321"
# Expected
# "9077746056551513321"
print(largestNumber([74, 21, 33, 51, 77, 51, 90, 60, 5, 56]))