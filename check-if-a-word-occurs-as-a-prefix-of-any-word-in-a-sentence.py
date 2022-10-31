def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    words = sentence.split(' ')
        
    for i in range(len(words)):
        word = words[i]
            
        if len(searchWord) > len(word):
            continue
        
        matched = True
        for j in range(len(searchWord)):
            if word[j] != searchWord[j]:
                matched = False
                break
                    
        if matched:
            return i + 1
                
    return -1

print(isPrefixOfWord("this problem is an easy problem", "pro"))