def isPalindrome(s: str) -> bool:
    alnum = ""
    for letter in s:
        if letter.isalnum():
            alnum += letter.lower()
    return alnum == alnum[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))
print(isPalindrome(" "))
