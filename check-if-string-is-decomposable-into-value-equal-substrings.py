class Solution:
    def isDecomposable(self, s: str) -> bool:
        current = 1
        hasTwo = False

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if current < 2:
                    return False
                
                rem = current % 3
                if rem > 0:
                    if rem == 2:
                        if hasTwo:
                            return False
                        hasTwo = True
                    else:
                        return False

                current = 0
            
            current += 1

        rem = current % 3
        if rem > 0:
            if rem == 2:
                if hasTwo:
                    return False
                hasTwo = True
            else:
                return False

        return hasTwo

solution = Solution()
assert solution.isDecomposable("66666666666677722") == True
assert solution.isDecomposable("000111000") == False
assert solution.isDecomposable("00011111222") == True
assert solution.isDecomposable("011100022233") == False