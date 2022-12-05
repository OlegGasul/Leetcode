class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k <= 0 or k > len(blocks):
            return -1
        
        w = 0
        b = 0

        for i in range(k):
            if blocks[i] == "W":
                w += 1
            else:
                b += 1

        result = w

        for j in range(k, len(blocks)):
            if blocks[j - k] == "W":
                w -= 1
            else:
                b -= 1
            
            if blocks[j] == "W":
                w += 1
            else:
                b += 1
            
            result = min(result, w)

        return result

solution = Solution()
assert solution.minimumRecolors("WBBWWBBWBW", 7) == 3
assert solution.minimumRecolors("WBWBBBW", 2) == 0