from collections import Counter

def commonChars(words):
    length = len(words)
    if length == 0:
        return []
        
    if length == 1:
        return list(words[0])
        
    letters = Counter(words[0])
        
    for i in range(1, length):
        counter = Counter(words[i])
            
        for ch, count in letters.items():
            letters[ch] = min(letters[ch], counter[ch])
                
    result = []
    for ch, count in letters.items():
        if count == 1:
            result.append(ch)
        else:
            result.extend([ch] * count)
                
    return result

print(commonChars([]))
print(commonChars(["bella"]))
print(commonChars(["bella", "label", "roller"]))
print(commonChars(["cool", "lock", "cook"]))