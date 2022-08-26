from time import sleep

def findDuplicates(nums):
    i = 0
    result = []

    while i < len(nums):
        if nums[i] < 0:
            i += 1
            continue
        
        if nums[i] != i + 1:
            if nums[nums[i] - 1] == nums[i]:
                result.append(nums[i])
                nums[i] = -1                
                i += 1
            else:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        else:
            i += 1

    return result

print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDuplicates([5, 4, 6, 7, 9, 3, 10, 9, 5, 6]))