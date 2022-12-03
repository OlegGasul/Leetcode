from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str):
        words1 = s1.split(' ')
        words2 = s2.split(' ')

        set1 = set()
        c1 = Counter(words1)
        for w, c in c1.items():
            if c == 1:
                set1.add(w)

        set1 -= set(words2)

        set2 = set()
        c2 = Counter(words2)
        for w, c in c2.items():
            if c == 1:
                set2.add(w)

        set2 -= set(words1)

        return list(set1 | set2)

solution = Solution()
print(solution.uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(solution.uncommonFromSentences("apple apple", "banana"))