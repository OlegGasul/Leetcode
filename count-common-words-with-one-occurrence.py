def countWords(words1, words2) -> int:
    duplicates = set()
    words1Set = set()
        
    for word in words1:
        if word in duplicates:
            continue
                
        if word in words1Set:
            words1Set.discard(word)
            duplicates.add(word)
            continue
            
        words1Set.add(word)
            
    duplicates = set()
    words2Set = set()
        
    for word in words2:
        if word in duplicates:
            continue
                
        if word in words2Set:
            words2Set.discard(word)
            duplicates.add(word)
            continue
            
        words2Set.add(word)
            
    return len(words1Set.intersection(words2Set))

print(countWords(["leetcode", "is", "amazing", "as", "is"], ["amazing", "leetcode", "is"]))
print(countWords(["b", "bb", "bbb"], ["a", "aa", "aaa"]))
print(countWords(["a", "ab"], ["a", "a", "a", "ab"]))