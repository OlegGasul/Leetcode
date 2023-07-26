from sortedcontainers import SortedSet

class Solution:
    def oddEvenJumps(self, arr) -> int:
        minSet = SortedSet()
        maxSet = SortedSet()
        
        length = len(arr)
        lastIndex = length - 1

        oddGraph = {}
        evenGraph = {}

        minSet.add((arr[-1], lastIndex))
        maxSet.add((-1 * arr[-1], lastIndex))

        for i in range(length - 2, -1, -1):
            value = arr[i]
            index = minSet.bisect_left((value, i))
            if index < len(minSet):
                val, j = minSet[index]
                oddGraph[i] = j

            index = maxSet.bisect_left((-1 * value, i))
            if index < len(maxSet):
                val, j = maxSet[index]
                evenGraph[i] = j
            
            minSet.add((arr[i], i))
            maxSet.add((-1 * arr[i], i))

        def check(index):
            step = 1

            while True:
                if index == lastIndex:
                    return 1
                
                if step % 2 == 0:
                    if not index in evenGraph:
                        break
                    index = evenGraph[index]
                else:
                    if not index in oddGraph:
                        break
                    index = oddGraph[index]
                
                step += 1
            
            return 0

        result = 0
        for i in range(length):
            result += check(i)

        return result


solution = Solution()
assert solution.oddEvenJumps([10, 13, 12, 14, 15]) == 2
assert solution.oddEvenJumps([2, 3, 1, 1, 4]) == 3