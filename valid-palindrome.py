def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        
        while right > left and not s[right].isalnum():
            right -= 1

        if left == right:
            break

        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1

    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("0P"))
print(isPalindrome(" "))
print(isPalindrome("race a car"))
print(isPalindrome(".,"))
