# https://leetcode.com/problems/matrix-block-sum/discuss/2502618/Python3-Simple-and-Very-Fast-with-Prefix-Sums-of-Prefix-Sums

def matrixBlockSum(mat, k: int):
    n, m = len(mat), len(mat[0])
    dp = [[mat[i][j] for j in range(m)] for i in range(n)]

    # Prefix Sums Left to Right
    for i in range(n):
        for j in range(m):
            dp[i][j] += (dp[i][j - 1] if j > 0 else 0)

    print(dp)

    # Prefix Sums of Sums Top to Bottom
    for j in range(m):
        for i in range(n):
            dp[i][j] += (dp[i - 1][j] if i > 0 else 0)

    print(dp)
                        
    # Update input Mat with sum per cell
    for i in range(n):
        for j in range(m):
            x1, x2 = max(0, j - k), min(j + k, m - 1)
            y1, y2 = max(0, i - k), min(i + k, n - 1)
            dy = dp[y1 - 1][x2] if y1 > 0 else 0
            dx = dp[y2][x1 - 1] if x1 > 0 else 0
            dz = dp[y1 - 1][x1 - 1] if (x1 > 0 and y1 > 0) else 0
            mat[i][j] = dp[y2][x2] - dy - dx + dz

    return mat

# [[1, 3, 6],
#  [4, 9, 15],
#  [7, 15, 24]]

# [[1, 3, 6],
#  [5, 12, 21],
#  [12, 27, 45]]

print(matrixBlockSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]], 1))