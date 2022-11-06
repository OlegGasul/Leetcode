class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        n = 1

        while n <= length // 2:
            if length % n != 0 :
                n += 1
                continue

            pattern = s[:n]
            j = 0
            result = True
            for i in range(n, length):
                if s[i] != pattern[j]:
                    result = False
                    break

                j += 1
                if j >= n:
                    j = 0

            if result:
                return True

            n += 1

        return False

solution = Solution()
print(solution.repeatedSubstringPattern("abab"))
print(solution.repeatedSubstringPattern("abcabcabcabc"))