class Solution:
    def rotateTheBox(self, box):
        rows = len(box)
        cols = len(box[0])

        for i in range(rows):
            empty = -1
            for j in range(cols - 1, -1, -1):
                if box[i][j] == ".":
                    if empty < 0:
                        empty = j
                elif box[i][j] == "*":
                    empty = -1
                elif box[i][j] == "#" and empty > 0:
                    box[i][j] = "."
                    box[i][empty] = "#"
                    empty -= 1
        
        result = []

        for j in range(cols):
            current = []
            for i in range(rows - 1, -1, -1):
                current.append(box[i][j])
            result.append(current)

        return result

solution = Solution()
assert solution.rotateTheBox([["#","#","*",".","*","."], ["#","#","#","*",".","."], ["#","#","#",".","#","."]]) == [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]