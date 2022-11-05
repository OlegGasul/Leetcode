class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        counts = [0] * len(s)
        strList = list(s)

        counts[0] = 1
        
        i = 1
        while i < len(strList):
            if i == 0:
                i = 1
                continue

            if strList[i - 1] == strList[i]:
                counts[i] += counts[i - 1] + 1

                if counts[i] == k:
                    for _ in range(k):
                        counts.pop(i)
                        strList.pop(i)
                        i -= 1
            else:
                counts[i] = 1

            i += 1

        return ''.join(strList)

solution = Solution()
print(solution.removeDuplicates("deeedbbcccbdaa", 3))
print(solution.removeDuplicates("pbbcggttciiippooaais", 2))