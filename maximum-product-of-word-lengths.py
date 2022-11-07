class Solution:
    def maxProduct(self, words) -> int:
        a = ord('a')
        
        masks = []
        for word in words:
            current = 0
            for ch in word:
                current |= 1 << (ord(ch) - a)
            masks.append(current)

        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if masks[i] & masks[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))

        return result

solution = Solution()
print(solution.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(solution.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(solution.maxProduct(["a", "aa", "aaa", "aaaa"]))