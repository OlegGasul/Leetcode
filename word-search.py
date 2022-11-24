class Solution:
    def exist(self, board, word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        length = len(word)

        def dfs(i, j, index, visited):
            visited.add((i, j))
            if index + 1 >= length:
                return True
            
            if i + 1 < rows and not (i + 1, j) in visited:
                if board[i + 1][j] == word[index + 1]:
                    if dfs(i + 1, j, index + 1, visited):
                        return True
                    else:
                        visited.remove((i + 1, j))

            if j + 1 < cols and not (i, j + 1) in visited:
                if board[i][j + 1] == word[index + 1]:
                    if dfs(i, j + 1, index + 1, visited):
                        return True
                    else:
                        visited.remove((i, j + 1))

            if i - 1 >= 0 and not (i - 1, j) in visited:
                if board[i - 1][j] == word[index + 1]:
                    if dfs(i - 1, j, index + 1, visited):
                        return True
                    else:
                        visited.remove((i - 1, j))

            if j - 1 >= 0 and not (i, j - 1) in visited:
                if board[i][j - 1] == word[index + 1]:
                    if dfs(i, j - 1, index + 1, visited):
                        return True
                    else:
                        visited.remove((i, j - 1))

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0, visited):
                        return True

        return False

solution = Solution()
print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))