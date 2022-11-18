import functools

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def compare(a, b):
            if len(a) == len(b):
                for i in range(len(a)):
                    if a[i] != b[i]:
                        return int(a[i]) - int(b[i])
                return 0
            else:
                return len(a) - len(b)

        nums = sorted(nums, key = functools.cmp_to_key(compare))

        return nums[-k]

solution = Solution()
print(solution.kthLargestNumber(["3", "6", "7", "10"], 4))
print(solution.kthLargestNumber(["2", "21", "12", "1"], 3))