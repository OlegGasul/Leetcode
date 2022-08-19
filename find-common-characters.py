def commonChars(words):
    length = len(words)
    if length == 1:
        return list(words[0])
    
    words.sort(key = lambda s: len(s))
    
    chars = set(words[0])

    for i in range(1, length):
        chars = chars.intersection(words[i])
        if len(chars) == 0:
            return []

    return list(chars)


print(commonChars(["bella", "label", "roller"]))