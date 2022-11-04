from collections import Counter

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum):
        if sum(colsum) != upper + lower:
            return []
        
        result = [[0] * len(colsum), [0] * len(colsum)]
        
        counter = Counter(colsum)
        
        upper -= counter[2]
        lower -= counter[2]
        
        if upper < 0 or lower < 0:
            return []
        
        for i in range(len(colsum)):
            s = colsum[i]
            
            if s == 2:
                result[0][i] = 1
                result[1][i] = 1
            elif s == 1:
                if upper:
                    result[0][i] = 1
                    upper -= 1
                elif lower:
                    result[1][i] = 1
                    lower -= 1
        
        return result

solution = Solution()
print(solution.reconstructMatrix(5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]))