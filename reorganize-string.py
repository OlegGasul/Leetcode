from collections import Counter

def checkIfOrganized(s: str) -> bool:
    length = len(s)

    if length == 1:
        return True

    if length == 2:
        return s[0] != s[1]

    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] or s[i] == s[i + 1]:
            return False

    return True

def reorganizeString(s: str) -> str:
    length = len(s)

    if checkIfOrganized(s):
        return s

    result = []

    counter = Counter(s)

    most = counter.most_common(1)
    if (most[0][1] * 2) - 1 > length:
        return ""
    
    most = counter.most_common(2)
    # print(most)

    while most:
        if len(most) == 1:
            result.append(most[0][0])
            break
        
        for freq in most:
            result.append(freq[0])
            
            counter[freq[0]] -= 1
            if counter[freq[0]] <= 0:
                del counter[freq[0]]

        most = counter.most_common(2)
        # print(most)
    
    return ''.join(result)
        


print(reorganizeString("aaabbcc"))
print(reorganizeString("aaab"))
print(reorganizeString("vvvlo"))