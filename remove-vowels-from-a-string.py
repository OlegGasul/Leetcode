class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        result = []

        for ch in s:
            if not ch in vowels:
                result.append(ch)

        return ''.join(result)

solution = Solution()
assert solution.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"
assert solution.removeVowels("aeiou") == ""