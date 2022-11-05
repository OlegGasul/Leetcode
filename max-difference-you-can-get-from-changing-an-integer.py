from collections import Counter

class Solution:
    def maxDiff(self, num: int) -> int:
        nums = [int(x) for x in list(str(num))]
        counter = Counter(nums)

        minimum = float('inf')
        maximum = float('-inf')

        def makeValue(fromNum, toNum):
            result = 0
            for i in nums:
                result *= 10
                result += toNum if i == fromNum else i

            return result

        mostCommon = counter.most_common()

        for v, c in mostCommon:
            fromNum = v
            minimum = min(minimum, makeValue(fromNum, 1 if nums[0] == fromNum else 0))
            maximum = max(maximum, makeValue(fromNum, 9))

        return maximum - minimum



solution = Solution()
print(solution.maxDiff(555))
print(solution.maxDiff(9))
print(solution.maxDiff(19))