from collections import deque

def maxSlidingWindow(nums, k: int):
    result = []
    queue = deque()

    for i in range(len(nums)):
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