from collections import Counter

def firstUniqChar(s: str) -> int:
    counter = Counter(s)
        
    for idx, ch in enumerate(s):
        if counter[ch] == 1:
            return idx
            
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))