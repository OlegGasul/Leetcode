import copy

def findLongestWord(s: str, dictionary) -> str:
    a = ord('a')
    
    def createMap(word):
        result = [0] * 26
        for i in range(len(s)):
            result[ord(s[i]) - a] += 1
        return result

    sMap = createMap(s)

    dictionary.sort()
    dictionary.sort(key = len, reverse = True)

    for word in dictionary:
        arr = copy.copy(sMap)
        flag = True
        
        for ch in word:
            k = ord(ch) - a
            arr[k] -= 1
            if arr[k] < 0:
                flag = False
                break

        if flag:
            return word

    return ""


print(findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(findLongestWord("abce",  ["abe", "abc"]))
print(findLongestWord("aewfafwafjlwajflwajflwafj", ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]))