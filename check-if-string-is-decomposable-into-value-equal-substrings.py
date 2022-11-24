class Solution:
    def isDecomposable(self, s: str) -> bool:
        counts = set()

        current = 1
        hasTwo = False
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if current < 2:
                    return False
                
                if current == 2:
                    if hasTwo:
                        return False
                    hasTwo = True
                else:
                    counts.add(current)
                    
                current = 0
            
            current += 1

        for n in counts:
            rem = n % 3

            if rem == 0:
                continue
            
            if hasTwo:
                if rem > 0:
                    return False
            else:
                if rem == 2:
                    hasTwo = True
                else:
                    return False

        return True

solution = Solution()
print(solution.isDecomposable("00011111222"))
print(solution.isDecomposable("000111000"))
print(solution.isDecomposable("00011111222"))
print(solution.isDecomposable("011100022233"))