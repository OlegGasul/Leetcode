def replaceElements(arr):
    greatest = arr[-1]
    arr[-1] = -1
        
    for i in reversed(range(len(arr) - 1)):
        temp = arr[i]
        arr[i] = greatest
        if temp > greatest:
            greatest = temp
                
    return arr

print(replaceElements([17, 18, 5, 4, 6, 1]))
print(replaceElements([400]))