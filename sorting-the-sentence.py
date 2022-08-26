import functools

def sortSentence(s: str) -> str:
    words = s.split(' ')
        
    def compare(a, b):
        return int(a[-1]) - int(b[-1])
        
    words = sorted(words, key = functools.cmp_to_key(compare))
        
    return ' '.join(map(lambda x: x[0:len(x) - 1], words))

print(sortSentence("is2 sentence4 This1 a3"))