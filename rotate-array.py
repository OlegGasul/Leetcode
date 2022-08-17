def rotate(nums, k: int) -> None:
    length = len(nums)
    
    if length == 0 or k == 0:
        return

    permutations = k % length
    if permutations == 0:
        return

    if permutations < length // 2:
        for i in range(permutations):
            nums.insert(0, nums.pop())
    else:
        for i in range(length - permutations):
            nums.append(nums.pop(0))
        

nums = [1, 2, 3, 4, 5, 6, 7]
print(list(nums))
rotate(nums, 6)
# [1, 2, 3, 4, 5, 6, 7]
# [7, 1, 2, 3, 4, 5, 6]
# [6, 7, 1, 2, 3, 4, 5]
# [5, 6, 7, 1, 2, 3, 4]
print(list(nums))