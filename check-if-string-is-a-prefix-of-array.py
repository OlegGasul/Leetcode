def isPrefixString(s: str, words) -> bool:
    index = 0
    length = len(s)
        
    for word in words:
        for i in range(len(word)):
            if index == length:
                return False
                
            if word[i] != s[index]:
                return False
            
            index += 1
                
        if index == length:
            return True
            
    return index == length

print(isPrefixString("iloveleetcode", ["i", "love", "leetcode", "apples"]))
print(isPrefixString("iloVeleetcode", ["i", "love", "leetcode", "apples"]))
print(isPrefixString("iloVeleetcode", ["i", "love"]))
print(isPrefixString("iloveleetco", ["i", "love", "leetcode", "apples"]))