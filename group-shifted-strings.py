from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)

        for s in strings:
            key = ""
            for i in range(1, len(s)):
                a = ord(s[i - 1])
                b = ord(s[i])
                
                key += str((b - a + 26) % 26) + 'a'
            
            groups[key].append(s)
        
        return groups.values()

solution = Solution()
print(solution.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]) == [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]])
print(solution.groupStrings(["a"]) == [["a"]])