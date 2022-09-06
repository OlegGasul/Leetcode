def winnerOfGame(colors: str) -> bool:
    a = 0
    b = 0
    aResult = 0
    bResult = 0
        
    for i in range(len(colors)):
        if colors[i] == "A":
            if b and b >= 3:
                bResult += b - 2
            
            b = 0
            a += 1
        elif colors[i] == "B":
            if a and a >= 3:
                aResult += a - 2
            
            a = 0
            b += 1

    if a >= 3:
        aResult += a - 2
    elif b >= 3:
        bResult += b - 2

    return aResult - bResult > 0

print(winnerOfGame("AAA"))
print(winnerOfGame("BBAAABBABBABB"))
print(winnerOfGame("AAAABBBB"))
