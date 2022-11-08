class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        
        result = 1
        counter = 1

        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                counter += 1
                result = i
                if counter == k:
                    return result

        if k - counter == 1:
            return n

        return -1

solution = Solution()
print(solution.kthFactor(12, 3))
print(solution.kthFactor(7, 2))
print(solution.kthFactor(4, 4))