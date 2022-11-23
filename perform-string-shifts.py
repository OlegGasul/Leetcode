class Solution:
    def stringShift(self, s: str, shift) -> str:
        total = 0
        for direction, count in shift:
            total += count if direction == 0 else -count
        
        total %= len(s)
        
        return ''.join(s[total:] + s[:total])

solution = Solution()
print(solution.stringShift("abc", [[0, 1], [1, 2]]))
print(solution.stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))