class Solution:
    def tictactoe(self, moves) -> str:
        # 1, 2, 4
        # 8, 16, 32
        # 64, 128, 256

        a = 0
        b = 0
        flag = True
        counter = 0

        def isWinner(value):
            for pattern in list([(1 + 2 + 4), (8 + 16 + 32), (64 + 128 + 256),
                (1 + 8 + 64), (2 + 16 + 128), (4 + 32 + 256),
                (1 + 16 + 256), (4 + 16 + 64)]):
                if pattern & value == pattern:
                    return True

        for x, y in moves:
            value = 1 << x * 3 + y
            if flag:
                a |= value
                if isWinner(a):
                    return "A"
            else:
                b |= value
                if isWinner(b):
                    return "B"

            flag = not flag
            counter += 1

        return "Draw" if counter == 9 else "Pending"

solution = Solution()
print(solution.tictactoe([[1, 2], [2, 1], [1, 0], [0, 0], [0, 1], [2, 0], [1, 1]]))
print(solution.tictactoe([[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
print(solution.tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))