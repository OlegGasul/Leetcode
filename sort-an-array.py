def insert(arr, value):
    length = len(arr)
    if length == 0:
        arr.append(value)
        return

    left = 0
    right = length - 1

    while left < right:
        middle = left + (right - left) // 2

        if value > arr[middle]:
            left = middle + 1
        else:
            right = middle - 1

    if  value < arr[left]:
        arr.insert(left, value)
    else:
        arr.insert(left + 1, value)

def sortArray(nums):
    result = []

    for x in nums:
        insert(result, x)

    return result

# print(sortArray([5, 2, 3, 1]))
# print(sortArray([5, 1, 1, 2, 0, 0]))
# [-4, 0, 4, 7]
# 9
print(sortArray([-4, 0, 7, 4, 9, -5, -1, 0, -7, -1]))

