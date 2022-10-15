import math

def countPoints(points, queries):
    result = []

    for query in queries:
        count = 0

        for point in points:
            dist = math.sqrt((query[0] - point[0]) ** 2 + (query[1] - point[1]) ** 2)
            if dist <= query[2]:
                count += 1

        result.append(count)

    return result
            

print(countPoints([[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]))
print(countPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]))