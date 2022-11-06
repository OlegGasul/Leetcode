class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        bits = [0] * (len(arr) + 2)
        
        ranges = [[0, 0] for _ in range(len(arr) + 2)]
        mCounts = 0
        result = -1

        for i in range(len(arr)):
            index = arr[i]
            if bits[index] == 1:
                continue

            bits[index] = 1

            if bits[index - 1] == 0 and bits[index + 1] == 0:
                first = index
                last = index
            else:
                if bits[index - 1] == 1:
                    first = ranges[index - 1][0]
                else:
                    first = index

                if bits[index + 1] == 1:
                    last = ranges[index + 1][1]
                else:
                    last = index

            if first != index:
                if ranges[first][1] - ranges[first][0] + 1 == m:
                    mCounts -= 1
            ranges[first] = [first, last]
            
            if last != index:
                if ranges[last][1] - ranges[last][0] + 1 == m:
                    mCounts -= 1
            ranges[last] = [first, last]

            if last - first + 1 == m:
                mCounts += 1

            if mCounts > 0:
                result = i + 1

        return result


solution = Solution()
print(solution.findLatestStep([3, 5, 1, 2, 4], 1))
print(solution.findLatestStep([3, 1, 5, 4, 2], 2))