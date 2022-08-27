def validPalindromeSubstring(s: str, left, right, deleted: bool) -> bool:
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while right > left and not s[right].isalnum():
            right -= 1

        if left == right:
            break

        if s[left].lower() != s[right].lower():
            if deleted:
                return False
            
            if right - left == 1:
                return True
            else:
                return validPalindromeSubstring(s, left + 1, right, True) or validPalindromeSubstring(s, left, right - 1, True)
        
        left += 1
        right -= 1

    return True

def validPalindrome(s: str) -> bool:
    return validPalindromeSubstring(s, 0, len(s) - 1, False)


# print(validPalindrome("abca"))
# print(validPalindrome("aba"))
# print(validPalindrome("abc"))
# print(validPalindrome("abcba"))
# print(validPalindrome("abcbad"))
# print(validPalindrome("abcbadd"))
print(validPalindrome("eeccccbebaeeabebccceea"))
print(validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))