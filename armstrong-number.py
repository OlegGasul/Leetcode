class Solution:
    def isArmstrong(self, n: int) -> bool:
        nstr = str(n)
        length = len(nstr)

        return sum([int(x) ** length for x in nstr]) == n

solution = Solution()
print(solution.isArmstrong(153))
print(solution.isArmstrong(123))