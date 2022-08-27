from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    counter = Counter(stones)
        
    result = 0
    for jewel in jewels:
        result += counter[jewel]
            
    return result

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("a", "AAA"))
print(numJewelsInStones("abb", "AAAa"))