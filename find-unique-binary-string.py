def findDifferentBinaryString(nums):
    values = set()
    
    for x in nums:
        values.add(int(x, 2))

    length = len(nums[0])
    result = []
    for i in range(2 ** length):
        if not i in values:
            return bin(i)[2:].zfill(length)


print(findDifferentBinaryString(["111", "011", "001"]))
print(findDifferentBinaryString(["00", "01"]))