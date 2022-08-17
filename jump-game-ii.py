# Input: nums = [2, 3, 1, 1, 4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

def doJump(nums, index, jumps) -> int:
    if nums[index] >= len(nums) - index - 1:
        return jumps + 1
    
    count = nums[index]
    start = index + 1
    end = start + count
    
    maxJump = -1
    maxJumpIndex = None

    for i in range(start, end):
        if nums[i] == 0:
            continue
        if nums[i] + i > maxJump:
            maxJump = nums[i] + i
            maxJumpIndex = i

    return doJump(nums, maxJumpIndex, jumps + 1)
    

    

def jump(nums) -> int:
    if len(nums) == 1:
        return 0
    
    return doJump(nums, 0, 0)



print(jump([2, 3, 1, 1, 4]))
print(jump([2, 3, 0, 1, 4]))
print(jump([5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]))
print(jump([1, 1, 1, 1]))
