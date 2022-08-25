def checkValid(matrix) -> bool:
    nums = set(range(1, len(matrix) + 1))
    
    for row in matrix:
        if set(row) != nums:
            return False
    
    for col in zip(*matrix):
        if set(col) != nums:
            return False
    
    return True
    

print(checkValid([
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]]))