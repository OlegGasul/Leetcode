class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1

        row = -1

        while left < right:
            middle = left + (right - left) // 2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                left = middle
                break
            
            if target < matrix[middle][0]:
                right = middle - 1
            else:
                left = middle + 1

        row = left

        left = 0
        right = cols - 1

        while left < right:
            middle = left + (right - left) // 2
            if target == matrix[row][middle]:
                return True

            if target < matrix[row][middle]:
                right = middle - 1
            else:
                left = middle + 1

        return matrix[row][left] == target

solution = Solution()
assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
assert solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False