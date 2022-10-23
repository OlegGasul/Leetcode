def alphabetBoardPath(target: str) -> str:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        
    letters = {}
        
    for i in range(len(board)):
        for j in range(len(board[i])):
            letters[board[i][j]] = [i, j]
                
    i = 0
    j = 0
        
    result = ""
        
    for k in range(len(target)):
        if not target[k] in letters:
            continue
        
        row, col = letters[target[k]]
        if row == i and col == j:
            result += "!"
            continue
                
        if target[k] == "z":
            if col < j:
                result += "L" * (j - col)
            elif col > j:
                result += "R" * (col - j)
                    
            if row < i:
                result += "U" * (i - row)
            elif row > i:
                result += "D" * (row - i)
        else:
            if row < i:
                result += "U" * (i - row)
            elif row > i:
                result += "D" * (row - i)
                
            if col < j:
                result += "L" * (j - col)
            elif col > j:
                result += "R" * (col - j)
                
        result += "!"
            
        i = row
        j = col
            
    return result

print(alphabetBoardPath("leet"))
print(alphabetBoardPath("zdz"))
print(alphabetBoardPath("aaaaaaaaa"))
print(alphabetBoardPath("aaaaa   aaaa"))