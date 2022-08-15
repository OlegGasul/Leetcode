def lengthOfLastWord(s: str) -> int:
    index = len(s) - 1
    chars = 0
    
    while index >= 0:
        if s[index] == ' ':
            if chars > 0:
                return chars
        else:
            chars += 1

        index -= 1

    return chars

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord("Hello World   "))
print(lengthOfLastWord("a"))