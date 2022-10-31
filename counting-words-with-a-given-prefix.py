def prefixCount(words, pref: str) -> int:
    result = 0
        
    for word in words:
        if len(pref) > len(word):
            continue
                
        matched = True
        for i in range(len(pref)):
            if word[i] != pref[i]:
                matched = False
                break
                    
        if matched:
            result += 1
                
    return result

print(prefixCount(["pay", "attention", "practice", "attend"], "at"))