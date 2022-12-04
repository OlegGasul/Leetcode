import bisect

class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        n = len(nums)
        prefixSum = [0] * n

        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        for i in range(len(queries)):
            index = bisect.bisect_left(prefixSum, queries[i])
            if index == n:
                queries[i] = n
            else:
                if prefixSum[index] == queries[i]:
                    queries[i] = index + 1
                else:
                    queries[i] = index

        return queries

solution = Solution()
assert solution.answerQueries([4, 5, 2, 1], [3, 10, 21]) == [2, 3, 4]
assert solution.answerQueries([2, 3, 4, 5], [1]) == [0]