import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        maxHeap = []
        for a, b in classes:
            a, b = a * 1.0, b * 1.0
            maxHeap.append((-profit(a, b), a, b))
        heapq.heapify(maxHeap)  # Heapify maxHeap cost O(N)

        while extraStudents:
            p, a, b = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-profit(a + 1, b + 1), a + 1, b + 1))
            extraStudents -= 1

        return sum(a / b for p, a, b in maxHeap) / len(classes)

solution = Solution()
print(solution.maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2))
print(solution.maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4))