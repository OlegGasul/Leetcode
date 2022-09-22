def buildArray(target, n: int):
    result = []
        
    k = 1
    for i in range(len(target)):
        if target[i] == k:
            result.append("Push")
        else:
            while target[i] > k:
                result.append("Push")
                result.append("Pop")
                k += 1
                    
            result.append("Push")
        k += 1
        
    return result

print(buildArray([1, 3], 3))
print(buildArray([1, 2, 3], 3))