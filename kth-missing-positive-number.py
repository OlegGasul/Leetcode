def findKthPositive(arr, k: int) -> int:
    if len(arr) == 0:
        return k
    
    counter = arr[0] - 1
    
    for i in range(1, len(arr)):
        if arr[i] - 1 == arr[i - 1]:
            continue
                
        missed = arr[i] - arr[i - 1] - 1
            
        if counter + missed >= k:
            return arr[i - 1] + k - counter
        else:
            counter += missed

    return k if counter >= k else arr[-1] + (k - counter)

print(findKthPositive([2, 3, 4, 7, 11], 5))
print(findKthPositive([5], 5))
print(findKthPositive([20], 3))
print(findKthPositive([20], 20))
print(findKthPositive([2], 1))
print(findKthPositive([2], 2))
