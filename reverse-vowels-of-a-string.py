def reverseVowels(s: str) -> str:
    vowels = { 'a', 'e', 'i', 'o', 'u' }
    arr = list(s)

    left = 0
    right = len(arr) - 1
    
    while left < right:
        leftChar = arr[left].lower()
        while left < right and not leftChar in vowels:
            left += 1
            leftChar = arr[left].lower()

        rightChar = arr[right].lower()
        while left < right and not rightChar in vowels:
            right -= 1
            rightChar = arr[right].lower()

        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return ''.join(arr)

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))