class Solution:
    def printVertically(self, s: str):
        words = []
        hasLetters = False
        
        for word in s.split(' '):
            letters = list(word)
            hasLetters = hasLetters or len(letters) > 0
            words.append(letters)
        
        result = []
        
        while hasLetters:
            current = ""
            hasLetters = False

            for word in words:
                current += word.pop(0) if len(word) > 0 else " "
                hasLetters = hasLetters or len(word) > 0

            result.append(current.rstrip())

        return result

solution = Solution()
print(solution.printVertically("HOW ARE YOU"))
print(solution.printVertically("TO BE OR NOT TO BE"))
print(solution.printVertically("CONTEST IS COMING"))