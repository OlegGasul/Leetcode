class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        
        mapping = {}
        visited = set()

        for i in range(len(words)):
            if not pattern[i] in mapping:
                if words[i] in visited:
                    return False
                mapping[pattern[i]] = words[i]
                visited.add(words[i])
            elif mapping[pattern[i]] != words[i]:
                return False
        
        return True

solution = Solution()
assert solution.wordPattern("abba", "dog cat cat dog") == True
assert solution.wordPattern("abba", "dog cat cat fish") == False
assert solution.wordPattern("aaaa", "dog cat cat dog") == False