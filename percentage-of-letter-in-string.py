import math

def percentageLetter(s: str, letter: str) -> int:
    count = 0
        
    for ch in s:
        if ch == letter:
            count += 1
                
        
    return math.floor((count / len(s)) * 100)

print(percentageLetter("foobar", "o"))
print(percentageLetter("jjjj", "k"))