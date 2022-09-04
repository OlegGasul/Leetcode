import heapq

def containVirus(isInfected) -> int:
    rows = len(isInfected)
    cols = len(isInfected[0])
        
    def collectArea(queue, i, j):
        isInfected[i][j] = 0
        queue.append([i, j])
            
        if j + 1 < cols and isInfected[i][j + 1] == 1:
            collectArea(queue, i, j + 1)
        if i + 1 < rows and isInfected[i + 1][j] == 1:
            collectArea(queue, i + 1, j)
        if j - 1 >= 0 and isInfected[i][j - 1] == 1:
            collectArea(queue, i, j - 1)
        if i - 1 >= 0 and isInfected[i - 1][j] == 1:
            collectArea(queue, i - 1, j)
                
    def collectAreas():
        areas = []
            
        for i in range(rows):
            for j in range(cols):
                if isInfected[i][j] == 1:
                    queue = []
                    collectArea(queue, i, j)
                    areas.append((len(queue), queue))
                        
        return areas

    def clculateWalls():
        walls = 0

        for i in range(rows):
            for j in range(cols):
                if isInfected[i][j] == 2:
                    if j + 1 < cols and isInfected[i][j + 1] == 0:
                        walls += 1
                    if i + 1 < rows and isInfected[i + 1][j] == 0:
                        walls += 1
                    if j - 1 >= 0 and isInfected[i][j - 1] == 0:
                        walls += 1
                    if i - 1 >= 0 and isInfected[i - 1][j] == 0:
                        walls += 1
        
        return walls


    walls = 0
        
    areas = collectAreas()
    print(isInfected)
    print('Areas')
    print(areas)
        
    hasAliveVirus = len(areas) > 0
        
    while hasAliveVirus:
        heapq.heapify(areas)
        
        area = heapq.heappop(areas)
        
        print(area)

        queue = area[1]
        for indecies in queue:
            isInfected[indecies[0]][indecies[1]] = 1
        
        # Mark as closed
        for indecies in queue:
            isInfected[indecies[0]][indecies[1]] = 2

        print('After wall')
        print(isInfected)
            
        hasAliveVirus = len(areas) > 0
            
        # Expand the virus
        while areas:
            area = heapq.heappop(areas)
            queue = area[1]
            
            for indecies in queue:
                isInfected[indecies[0]][indecies[1]] = 1
            
            for indecies in queue:
                i = indecies[0]
                j = indecies[1]
                
                if j + 1 < cols and isInfected[i][j + 1] == 0:
                    isInfected[i][j + 1] = 1
                if i + 1 < rows and isInfected[i + 1][j] == 0:
                    isInfected[i + 1][j] = 1
                if j - 1 >= 0 and isInfected[i][j - 1] == 0:
                    isInfected[i][j - 1] = 1
                if i - 1 >= 0 and isInfected[i - 1][j] == 0:
                    isInfected[i - 1][j] = 1

        print('After expansion')
        print(isInfected)

        if hasAliveVirus:
            areas = collectAreas()
            
    return clculateWalls()

print(containVirus([
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1]]))

# print(containVirus([
#     [0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0]]))