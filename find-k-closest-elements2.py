import heapq

def findClosestElements(arr, k: int, x: int):
    length = len(arr)
    left = 0
    right = k
    
    while right < len(arr):
        if arr[left] == arr[right]:
            left += 1
            right += 1
            continue
        
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
            right += 1
        else:
            break
    
    return arr[left : right]
    

print(findClosestElements([1, 2, 3, 4, 5], 4, 3))
print(findClosestElements([1, 2, 3, 9, 10], 2, 4))
print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 10))
print(findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))