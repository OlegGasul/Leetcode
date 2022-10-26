def countAsterisks(s: str) -> int:
    parts = s.split('|')
        
    i = 0
    result = 0
        
    while i < len(parts):
            
        for ch in parts[i]:
            if ch == '*':
                result += 1
            
        i += 2
            
    return result

print(countAsterisks("l|*e*et|c**o|*de|"))
print(countAsterisks("yo|uar|e**|b|e***au|tifu|l"))