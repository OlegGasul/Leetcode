import bisect

def medianSlidingWindow(nums, k: int):
    window = sorted(nums[:k])
    result = []

    right = k
    while right <= len(nums):
        window = nums[right - k : right]
        window.sort()
        
        if k % 2 == 0:
            result.append((window[k // 2] + window[k // 2 - 1]) / 2)
        else:
            result.append(window[k // 2])

        window.remove(nums[right - k])
        bisect.insort(window, nums[right - 1])

        right += 1

    return result
            
print(medianSlidingWindow([1, 4, 2, 3], 4))
print(medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))