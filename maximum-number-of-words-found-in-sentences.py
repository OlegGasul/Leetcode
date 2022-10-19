def mostWordsFound(sentences) -> int:
    result = 0
        
    for words in sentences:
        result = max(result, len(words.split(' ')))
            
    return result

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))