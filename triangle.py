def minimumTotal(triangle) -> int:
    def minimum(i, j):
        if len(triangle) - 1 == i:
            return min(triangle[i][j], triangle[i][j])
        return triangle[i][j] + min(minimum(i + 1, j), minimum(i + 1, j + 1))

    return minimum(0, 0)


print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
print(minimumTotal([[-10]]))
