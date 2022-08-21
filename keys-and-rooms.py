def canVisitAllRooms(rooms) -> bool:
    length = len(rooms)
    if length == 1:
        return True
    
    indexes = [0]
    visited = set()
    
    while indexes:
        index = indexes.pop()
        if not index in visited:
            visited.add(index)
            indexes += rooms[index]
    
    return len(visited) == length

        

# print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
# print(canVisitAllRooms([[1], [2], [3], []]))
print(canVisitAllRooms([[1], [2, 5], [3], [4, 1], [5], [2]]))