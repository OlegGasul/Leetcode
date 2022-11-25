from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        
        hasOdd = False
        for value, count in counter.items():
            if count % 2 != 0:
                if hasOdd:
                    return False
                hasOdd = True
        
        return True

solution = Solution()
assert solution.canPermutePalindrome("code") == False
assert solution.canPermutePalindrome("aab") == True
assert solution.canPermutePalindrome("carerac") == True