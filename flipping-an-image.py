class Solution:
    def flipAndInvertImage(self, image):
        for row in image:
            for i in range(len(row) // 2):
                row[i], row[len(row) - i - 1] = row[len(row) - i - 1], row[i]
                
                row[i] = 1 if row[i] == 0 else 0
                row[len(row) - i - 1] = 1 if row[len(row) - i - 1] == 0 else 0

            if len(row) % 2 != 0:
                row[len(row) // 2] = 1 if row[len(row) // 2] == 0 else 0

        return image

solution = Solution()
print(solution.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(solution.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))