class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        
        while i < len(name):
            letter = name[i]
            typedLetter = typed[j]
            if letter != typedLetter:
                return False
            
            count = 1
            i += 1
            while i < len(name) and name[i] == letter:
                i += 1
                count += 1
                
            countTyped = 1
            j += 1
            while j < len(typed) and typed[j] == typedLetter:
                j += 1
                countTyped += 1
            
            if count > countTyped:
                return False
                
        return True

solution = Solution()
assert solution.isLongPressedName("alex", "aaleex") == True
assert solution.isLongPressedName("saeed", "ssaaedd") == False