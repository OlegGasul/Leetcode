class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = False

        for i in range(len(s)):
            record = s[i]
            
            if record == "A":
                if absent:
                    return False
                absent = True
            elif record == "L" and i >= 2 and s[i - 1] == s[i - 2] == "L":
                return False

        return True

solution = Solution()
print(solution.checkRecord("PPALLP"))
print(solution.checkRecord("PPALLL"))