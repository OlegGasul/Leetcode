from time import sleep

def findErrorNums(nums):
    length = len(nums)

    i = 0
    repeated = 0
    
    while i < length:
        if nums[i] > 0 and nums[i] != i + 1:
            if nums[nums[i] - 1] == nums[i]:
                repeated = nums[i]
                nums[i] = 0
            else:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
                continue

        i += 1

    return [repeated, (length * (length + 1)) // 2 - sum(nums)]
    


print(findErrorNums([3, 2, 4, 1, 1]))
print(findErrorNums([1, 2, 2, 4]))
print(findErrorNums([3, 2, 2]))
print(findErrorNums([8, 7, 3, 5, 3, 6, 1, 4]))
