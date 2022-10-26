def isPathCrossing(path: str) -> bool:
    visited = set()
    directions = {
        'N': [0, 1],
        'S': [0, -1],
        'E': [1, 0],
        'W': [-1, 0]
    }
        
    start = (0, 0)
    visited.add(start)
        
    for direction in path:
        move = directions[direction]
        move = (start[0] + move[0], start[1] + move[1])
            
        if move in visited:
            return True
            
        visited.add(move)
        start = move
            
    return False

print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))