class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        prev = s[0]
        bits = [1]
        
        for i in range(1, len(s)):
            if s[i] == prev:
                bits[-1] += 1
            else:
                bits.append(1)
                prev = s[i]
                
        result = 0
        for i in range(1, len(bits)):
            result += min(bits[i], bits[i - 1])
            
        return result

solution = Solution()
print(solution.countBinarySubstrings("00110011"))
print(solution.countBinarySubstrings("10101"))