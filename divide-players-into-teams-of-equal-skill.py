from collections import Counter

class Solution:
    def dividePlayers(self, skill) -> int:
        if len(skill) == 2:
            return skill[0] * skill[1]
        
        total = sum(skill)
        half = len(skill) // 2
        if total % half != 0:
            return -1
        
        totalForTeam = total // half
        counter = Counter()
        result = 0

        for n in skill:
            reminder = totalForTeam - n
            if reminder in counter:
                counter[reminder] -= 1
                if not counter[reminder]:
                    del counter[reminder]
                result += reminder * n
            else:
                counter[n] += 1
        
        return result if not counter else -1

solution = Solution()
assert solution.dividePlayers([3, 2, 5, 1, 3, 4]) == 22
assert solution.dividePlayers([3, 4]) == 12
