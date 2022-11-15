class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        k = 0
        l = 0
        
        def next():
            nonlocal k, l

            item = mat[k][l]
            l += 1
            if l >= cols:
                k += 1
                l = 0
            
            return item

        result = [[0 for x in range(c)] for y in range(r)]

        for i in range(r):
            for j in range(c):
                result[i][j] = next()

        return result
        
solution = Solution()
print(solution.matrixReshape([[1, 2], [3, 4]], 1, 4))
print(solution.matrixReshape([[1, 2], [3, 4]], 2, 4))