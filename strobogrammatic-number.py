class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return False
        
        matches = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        n = len(num)
        for i in range(n // 2):
            if not num[i] in matches or not num[n - i - 1] in matches:
                return False
            
            if matches[num[i]] != num[n - i - 1]:
                return False

        if n % 2 != 0 and not num[n // 2] in ('0', '1', '8'):
            return False
        
        return True

solution = Solution()
assert solution.isStrobogrammatic("69") == True
assert solution.isStrobogrammatic("88") == True
assert solution.isStrobogrammatic("962") == False