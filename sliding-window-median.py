import bisect

def medianSlidingWindow(nums, k: int):
    window = sorted(nums[:k])
    result = []
    length = len(nums)

    for i in range(k, length + 1):
        if k % 2 == 0:
            result.append((window[k // 2] + window[k // 2 - 1]) / 2)
        else:
            result.append(window[k // 2])

        if i < length:
            window.remove(nums[i - k])
            bisect.insort(window, nums[i])

    return result
            
print(medianSlidingWindow([1, 4, 2, 3], 4))
print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))