import heapq

def maxAverageRatio(classes, extraStudents: int) -> float:
    length = len(classes)
    def comparator(a, b):
        return a[1] - b[1]

    dp = []
    for i in range(length):
        heapq.heappush(dp, (classes[i][0] / classes[i][1], i))
    heapq.heapify(dp)

    # print(classes)
    # print()

    while extraStudents:
        value = heapq.heappop(dp)
        
        # print(value)

        clazz = classes[value[1]]
        clazz[0] += 1
        clazz[1] += 1
        
        heapq.heappush(dp, (clazz[0] / clazz[1], value[1]))
        heapq.heapify(dp)

        # print(dp)
        # print(classes)
        # print()

        extraStudents -= 1

    result = 0
    for i in range(length):
        result += classes[i][0] / classes[i][1]
    result = result / length

    # print(dp)
    # print(classes)

    return result

print(maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
print(maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))