def minimumMoves(s: str) -> int:
    result = 0
        
    i = 0
    while i < len(s):
        if s[i] == "O":
            i += 1
            continue
            
        result += 1
        i += 3
            
    return result

print(minimumMoves("XXX"))
print(minimumMoves("XXOX"))
print(minimumMoves("OOOO"))