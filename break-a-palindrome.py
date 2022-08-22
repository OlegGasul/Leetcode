def breakPalindrome(palindrome: str) -> str:
    length = len(palindrome)
    if len(palindrome) == 1:
        return ""

    chars = list(palindrome)
    for i in range(length // 2):
        if chars[i] != 'a':
            chars[i] = 'a'
            return ''.join(chars)

    chars[-1] = 'b'
    return ''.join(chars)


print(breakPalindrome("abccba"))
print(breakPalindrome("aba"))
print(breakPalindrome("aabaa"))
print(breakPalindrome("a"))
print(breakPalindrome("aa"))
print(breakPalindrome("aabbaa"))