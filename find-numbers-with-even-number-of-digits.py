def findNumbers(nums) -> int:
    return sum([1 if len(str(x)) % 2 == 0 else 0 for x in nums])

print(findNumbers([12, 345, 2, 6, 7896]))
print(findNumbers([555, 901, 482, 1771]))