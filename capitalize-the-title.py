def capitalizeTitle(title: str) -> str:
    words = title.split(' ')

    for i in range(len(words)):
        word = list(words[i])
        wordLen = len(word)

        if wordLen < 3:
            start = 0
        else:
            start = 1
            word[0] = word[0].upper()
        
        for j in range(start, wordLen):
            word[j] = word[j].lower()

        words[i] = ''.join(word)

    return ' '.join(words)

        

print(capitalizeTitle("capiTalIze tHe titLe"))
print(capitalizeTitle("First leTTeR of EACH Word"))
print(capitalizeTitle("L hV"))