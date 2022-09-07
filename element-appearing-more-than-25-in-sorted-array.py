def findSpecialInteger(arr) -> int:
    length = len(arr)
    arr.append(-1)
        
    countNeeded = length // 4
        
    count = 0
    for i in range(length):
        if arr[i] != arr[i - 1]:
            if count > countNeeded:
                return arr[i - 1]
            count = 1
        else:
            count += 1
                
    if count > countNeeded:
        return arr[i]
    else:
        return -1

print(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]))