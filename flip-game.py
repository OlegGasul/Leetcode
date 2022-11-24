class Solution:
    def generatePossibleNextMoves(self, currentState: str):
        result = []
        
        for i in range(len(currentState) - 1):
            if currentState[i : i + 2] == "++":
                result.append(currentState[ : i] + "--" + currentState[i + 2 : ])
        
        return result

solution = Solution()
print(solution.generatePossibleNextMoves("++++"))
print(solution.generatePossibleNextMoves("+"))
print(solution.generatePossibleNextMoves("++++++++++++"))