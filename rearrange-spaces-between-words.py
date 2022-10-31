def reorderSpaces(text: str) -> str:
    spaces = 0
    words = []
        
    wordStarted = False
    wordStartedIndex = 0
        
    for i in range(len(text)):
        ch = text[i]
            
        if ch == ' ':
            spaces += 1
                
            if wordStarted:
                words.append(text[wordStartedIndex : i])
            wordStarted = False
        elif not wordStarted:
            wordStarted = True
            wordStartedIndex = i
                
    if wordStarted:
        words.append(text[wordStartedIndex :])

    if len(words) > 1:
        extraSpace = spaces % (len(words) - 1)
        spaces = ' ' * (spaces // (len(words) - 1))
        extraSpace = ' ' * extraSpace
    else:
        extraSpace = ' ' * spaces
        spaces = ''

    result = spaces.join(words)
    if extraSpace:
        result += extraSpace
            
    return result

print(reorderSpaces("  this   is  a sentence "))