def finalValueAfterOperations(operations) -> int:
    result = 0
        
    for op in operations:
        result += 1 if "+" in op else -1
                
    return result

print(finalValueAfterOperations(["--X", "X++", "X++"]))
print(finalValueAfterOperations(["++X", "++X", "X++"]))
print(finalValueAfterOperations(["X++", "++X", "--X", "X--"]))