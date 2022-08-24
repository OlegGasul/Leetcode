def fullJustify(words, maxWidth: int):
    result = []

    while words:
        temp = []

        length = maxWidth
        space = False
        while words and len(words[0]) + (1 if space else 0) < length:
            word = words.pop(0)
            
            length -= len(word) + (1 if space else 0)
            temp.append(word)
            space = True

        result.append(temp)

    lines = []

    while result:
        isLastLine = len(result) == 1

        line = result.pop(0)

        count = 0
        for i in range(len(line)):
            count += len(line[i])

        if len(line) > 1:
            spaces = ' ' * ((maxWidth - count) // (len(line) - 1))
            lines.append(spaces.join(line))
        else:
            lines.append(line.pop().ljust(maxWidth, ' '))

    return lines



print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))