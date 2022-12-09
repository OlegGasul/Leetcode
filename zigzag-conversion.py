class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [''] * numRows
        counter = 0
        direction = 1

        for i in range(len(s)):
            rows[counter] += s[i]
            counter += direction
            
            if counter >= numRows:
                direction = -1
                counter = numRows - 2
            elif counter < 0:
                direction = 1
                counter = 1

        result = ''
        for r in rows:
            result += ''.join(r)

        return result

solution = Solution()
assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"