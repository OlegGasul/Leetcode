def maxVowels(s: str, k: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
        
    current = 0
    maximum = 0
        
    for i in range(k):
        if s[i] in vowels:
            current += 1
                
    maximum = current
        
    for i in range(k, len(s)):
        if s[i - k] in vowels:
            current -= 1
        if s[i] in vowels:
            current += 1
        if current > maximum:
            maximum = current

    return maximum

print(maxVowels("abciiidef", 3))
print(maxVowels("aeiou", 2))
print(maxVowels("leetcode", 2))