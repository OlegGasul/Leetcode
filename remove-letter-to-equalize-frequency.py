from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        values = list(set(counter.values()))
        
        if len(values) == 1 and values[0] == 1:
            return True
        
        if len(values) != 2:
            return False
        
        if abs(values[0] - values[1]) > 1:
            return False
        
        return True
        
solution = Solution()
assert solution.equalFrequency("abcc") == True
assert solution.equalFrequency("aazz") == False