def minimumTotal2(triangle) -> int:
    def minimum(i, j):
        if len(triangle) - 1 == i:
            return min(triangle[i][j], triangle[i][j])
        return triangle[i][j] + min(minimum(i + 1, j), minimum(i + 1, j + 1))

    return minimum(0, 0)

def minimumTotal(triangle) -> int:
    for i in range(1, len(triangle)):        
        for j in range(i + 1):
            temp1, temp2 = float('inf'), float('inf')
            
            if j - 1 >= 0:
                temp1 = triangle[i - 1][j - 1]
            
            if j < i:
                temp2 = triangle[i - 1][j]
            
            triangle[i][j] = min(temp1, temp2) + triangle[i][j]

    return min(triangle[-1])
        

print(minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
# print(minimumTotal([[-10]]))
