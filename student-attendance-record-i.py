def checkRecord(s: str) -> bool:
    absent = 0
    late = 0
        
    for ch in s:
        if ch == "P":
            late = 0
        elif ch == "A":
            absent += 1
            if absent > 1:
                return False
            late = 0
        elif ch == "L":
            late += 1
            if late >= 3:
                return False
                
    return True

print(checkRecord("PPALLP"))
print(checkRecord("PPALLL"))