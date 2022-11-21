class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        return sorted(list(set(arr1).intersection(set(arr2)).intersection(set(arr3))))

solution = Solution()
print(solution.arraysIntersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))