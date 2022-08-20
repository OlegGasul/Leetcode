def intervalIntersection(firstList, secondList):
    result = []

    left = 0
    right = 0

    while left < len(firstList) and right < len(secondList):
        int1 = firstList[left]
        int2 = secondList[right]

        start = max(int1[0], int2[0])
        end = min(int1[1], int2[1])

        if end >= start:
            result.append([start, end])
                
        if int1[1] > int2[1]:
            right += 1
        else:
            left += 1

    return result


print(intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]]))

print(intervalIntersection(
    [[5, 10], [13, 23], [24, 25]],
    [[1, 4], [8, 12], [15, 24], [25, 26]]))