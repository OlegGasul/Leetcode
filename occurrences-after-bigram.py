def findOcurrences(text: str, first: str, second: str):
    words = text.split(' ')
        
    result = []
        
    for i in range(len(words) - 2):
        if words[i] == first and words[i + 1] == second:
            result.append(words[i + 2])
                
    return result

print(findOcurrences("alice is a good girl she is a good student", "a", "good"))