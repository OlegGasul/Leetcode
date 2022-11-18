class Solution:
    def merge(self, mNums, m: int, nNums, n: int) -> None:
        index = m + n - 1
        mIndex = m - 1
        nIndex = n - 1

        while index >= 0:
            if nIndex < 0:
                return
            
            if mIndex < 0:
                mNums[index] = nNums[nIndex]
                nIndex -= 1
            else:
                if mNums[mIndex] > nNums[nIndex]:
                    mNums[index] = mNums[mIndex]
                    mIndex -= 1
                else:
                    mNums[index] = nNums[nIndex]
                    nIndex -= 1
            
            index -= 1

solution = Solution()

nums = [1, 2, 3, 0, 0, 0]
solution.merge(nums, 3, [2, 5, 6], 3)
print(nums)

nums = [1]
solution.merge(nums, 1, [], 0)
print(nums)