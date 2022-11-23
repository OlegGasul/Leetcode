class Solution:
    def toHexspeak(self, num: str) -> str:
        if num == "0":
            return "O"
        
        mapping = {
            0: 'O',
            1: 'I',
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }

        n = int(num)
        result = []

        while n > 0:
            rem = n % 16
            if rem >= 2 and rem <= 9:
                return "ERROR"
            result.append(mapping[rem])
            n //= 16

        return ''.join(reversed(result))

solution = Solution()
print(solution.toHexspeak("257"))
print(solution.toHexspeak("3"))