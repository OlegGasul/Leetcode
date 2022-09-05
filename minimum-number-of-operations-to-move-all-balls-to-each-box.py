import copy

def minOperations(boxes: str):
    length = len(boxes)

    fromLeft = []
    fromRight = []

    for i in range(length):
        if not fromLeft:
            fromLeft.append([])
        else:
            fromLeft.append(copy.copy(fromLeft[-1]))
        
        for j in range(len(fromLeft[-1])):
            fromLeft[-1][j] += 1
        
        if boxes[i] == "1":
            fromLeft[-1].append(0)

        if not fromRight:
            fromRight.insert(0, [])
        else:
            fromRight.insert(0, copy.copy(fromRight[0]))

        for j in range(len(fromRight[0])):
            fromRight[0][j] += 1

        if boxes[length - i - 1] == "1":
            fromRight[0].append(0)

    result = [0] * length

    for i in range(length):
        result[i] = sum(fromLeft[i]) + sum(fromRight[i])
    
    return result

print(minOperations("110"))
print(minOperations("001011"))