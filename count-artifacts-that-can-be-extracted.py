class Solution:
    def digArtifacts(self, n: int, artifacts, dig) -> int:
        cells = {}
        artMap = {}

        for i in range(len(artifacts)):
            x1, y1, x2, y2 = artifacts[i]
            cells[i] = (x2 - x1 + 1) * (y2 - y1 + 1)

            for j in range(x1, x2 + 1):
                for k in range(y1, y2 + 1):
                    artMap[(j, k)] = i

        result = 0
        for x, y in dig:
            if (x, y) in artMap:
                cells[artMap[(x, y)]] -= 1
                if cells[artMap[(x, y)]] == 0:
                    result += 1
        
        return result

solution = Solution()
print(solution.digArtifacts(2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1]]))
print(solution.digArtifacts(2, [[0, 0, 0, 0], [0, 1, 1, 1]], [[0, 0], [0, 1], [1, 1]]))