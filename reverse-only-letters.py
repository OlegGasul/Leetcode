def reverseOnlyLetters(s: str) -> str:
    chars = list(s)

    left = 0
    right = len(chars) - 1

    while left < right:
        while not chars[left].isalpha() and left < right:
            left += 1

        while not chars[right].isalpha() and left < right:
            right -= 1

        if right - left == 1 and (not chars[left].isalpha() or not chars[right].isalpha()):
            break

        chars[left], chars[right] = chars[right], chars[left]
        
        left += 1
        right -= 1
        
    return ''.join(chars)

print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(reverseOnlyLetters("1A + 2B = 3C"))