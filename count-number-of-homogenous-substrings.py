from collections import Counter

def countHomogenous(s: str) -> int:
    result = 0
    counter = 1
    
    counter = Counter()
    index = 0

    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            if i - index > 1:
                counter[s[i - 1]] += i - index
            index = i
        
        counter[s[index : i]] += 1

    counter[s[index : i + 1]] += 1
    
    # print(counter.most_common())

    return sum(counter.values())

# print(countHomogenous("abbcccaa"))
print(countHomogenous("aaaaa"))