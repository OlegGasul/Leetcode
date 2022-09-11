def judgeCircle(moves: str) -> bool:
    i = 0
    j = 0
        
    for move in moves:
        if move == "U":
            i -= 1
        elif move == "R":
            j += 1
        elif move == "D":
            i += 1
        elif move == "L":
            j -= 1
                
    return i == 0 and j == 0

print(judgeCircle("UD"))
print(judgeCircle("LL"))