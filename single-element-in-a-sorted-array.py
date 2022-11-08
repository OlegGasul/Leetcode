class Solution:
    def singleNonDuplicate(self, nums) -> int:
        length = len(nums)
        
        left = 0
        right = length - 1

        while left < right:
            middle = left + (right - left) // 2

            current = nums[middle]
            leftValue = nums[middle - 1] if middle > 0 else -1
            rightValue = nums[middle + 1] if middle < length - 1 else -1

            if current != leftValue and current != rightValue:
                return current

            if current == leftValue:
                if (middle + 1) % 2 != 0:
                    right = middle - 1
                else:
                    left = middle + 1
            elif current == rightValue:
                if (length - middle) % 2 != 0:
                    left = middle + 1
                else:
                    right = middle - 1

        return nums[left]

solution = Solution()
print(solution.singleNonDuplicate([1]))
print(solution.singleNonDuplicate([1, 1, 2]))
print(solution.singleNonDuplicate([1, 2, 2]))
print(solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))