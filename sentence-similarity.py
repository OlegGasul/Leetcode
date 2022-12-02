class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs) -> bool:
        n1 = len(sentence1)
        n2 = len(sentence2)

        if n1 != n2:
            return False

        pairs = set()
        for a, b in similarPairs:
            pairs.add((a, b))

        for i in range(n1):
            a, b = sentence1[i], sentence2[i]
            if a == b or (a, b) in pairs or (b, a) in pairs:
                continue
            
            return False
        
        return True

solution = Solution()
assert solution.areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]) == True
assert solution.areSentencesSimilar(["great"], ["great"], []) == True
assert solution.areSentencesSimilar(["great"], ["doubleplus", "good"], [["great", "doubleplus"]]) == False