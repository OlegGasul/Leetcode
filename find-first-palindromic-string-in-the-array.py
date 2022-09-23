def firstPalindrome(words) -> str:
    for word in words:
        isPalindrome = True
        length = len(word)
            
        for i in range(length // 2):
            if word[i] != word[length - i - 1]:
                isPalindrome = False
                break
                    
        if isPalindrome:
            return word
            
    return ""

print(firstPalindrome(["abc", "car", "ada", "racecar", "cool"]))
print(firstPalindrome(["notapalindrome", "racecar"]))
print(firstPalindrome(["def", "ghi"]))