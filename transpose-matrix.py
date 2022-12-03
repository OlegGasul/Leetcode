class Solution:
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        result = [[0 for x in range(rows)] for y in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
        
        return result

solution = Solution()
assert solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert solution.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]