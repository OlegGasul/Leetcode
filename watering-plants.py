def wateringPlants(plants, capacity: int) -> int:
    plants.insert(0, -1)
        
    current = capacity
        
    i = 1
    steps = 0
        
    while i < len(plants):
        if current < plants[i]:
            steps += (i - 1) * 2
            current = capacity
            
        steps += 1
        current -= plants[i]
        i += 1
            
    return steps

print(wateringPlants([2, 2, 3, 3], 5))
print(wateringPlants([1, 1, 1, 4, 2, 3], 4))
print(wateringPlants([7, 7, 7, 7, 7, 7, 7], 8))