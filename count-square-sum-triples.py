class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i * i for i in range(1, n + 1)]

        result = 0

        for i in range(len(squares)):
            a = squares[i]

            for j in range(i + 1, len(squares)):
                b = squares[j]

                if a + b > squares[-1]:
                    break
        
                result += 2 * (a + b in squares)
                
        return result

solution = Solution()
print(solution.countTriples(5))
print(solution.countTriples(10))