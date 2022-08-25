from collections import deque

def maxSlidingWindow(nums, k: int):
    if k == 0:
        return []

    if k == 1:
        return nums

    length = len(nums)

    if k == length:
        return [max(nums)]
    
    result = []
    queue = deque()

    for i in range(length):
        num = nums[i]
            
        if queue and queue[0] <= i - k:
            queue.popleft()

        while queue and nums[queue[-1]] <= num:
            queue.pop()

        queue.append(i)

        if i + 1 >= k:
            result.append(nums[queue[0]])
    return result


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([1, 2, 3, 4, 5, 6], 3))
print(maxSlidingWindow([1, 2, 3, 4, 5, 6], 6))