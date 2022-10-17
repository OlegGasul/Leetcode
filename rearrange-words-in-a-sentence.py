import functools

def arrangeWords(text: str) -> str:
    words = text.split(' ')
        
    def compare(a, b):
        return len(a) - len(b)
            
    words = sorted(words, key = functools.cmp_to_key(compare))
    
    words[0] = words[0][0].upper() + words[0][1:]
    for i in range(1, len(words)):
        words[i] = words[i][0].lower() + words[i][1:]
        
    return ' '.join(words)

print(arrangeWords("Leetcode is cool"))
print(arrangeWords("Keep calm and code on"))