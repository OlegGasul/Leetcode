class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        result = 1
        for i in range(left, right + 1):
            result *= i

        result = list(str(result))
        count = 0
        while result[-1] == "0":
            result.pop()
            count += 1

        if len(result) > 10:
            result = result[0:5] + ['...'] + result[-5:]

        return ''.join(result) + 'e' + str(count)

solution = Solution()
assert solution.abbreviateProduct(1, 4) == "24e0"
assert solution.abbreviateProduct(2, 11) == "399168e2"
assert solution.abbreviateProduct(371, 375) == "7219856259e3"