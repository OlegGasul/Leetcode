from collections import Counter

class Solution:
    def removeAnagrams(self, words):
        if not words:
            return list()
        
        prev = Counter(words[0])

        i = 1
        while i < len(words):
            current = Counter(words[i])
            if current == prev:
                words.pop(i)
            else:
                prev = current
                i += 1
        
        return words

solution = Solution()
assert solution.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]) == ["abba", "cd"]