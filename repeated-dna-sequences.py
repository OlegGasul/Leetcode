from collections import Counter

def findRepeatedDnaSequences(s: str):
    counter = Counter()
    
    for i in range(len(s) - 10 + 1):
        counter[s[i : i + 10]] += 1
        
    result = []
    
    for seq, count in counter.most_common():
        if count < 2:
            break
        result.append(seq)
            
    return result

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))