def findWords(words):
    first = set(list("qwertyuiop"))
    second = set(list("asdfghjkl"))
    third = set(list("zxcvbnm"))

    result = []

    for word in words:
        chars = set([x.lower() for x in list(word)])
        size = len(chars)

        if len(chars.intersection(first)) == size or len(chars.intersection(second)) == size or len(chars.intersection(third)) == size:
            result.append(word)
        
    return result


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(findWords(["adsdf", "sfd"]))