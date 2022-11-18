class Solution:
    def numberOfLines(self, widths, s: str):
        lines = 1
        a = ord('a')

        pixels = 0
        for ch in s:
            current = widths[ord(ch) - a]
            if pixels + current > 100:
                lines += 1
                pixels = 0
            
            pixels += current

        return [lines, pixels]

solution = Solution()
print(solution.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
print(solution.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))