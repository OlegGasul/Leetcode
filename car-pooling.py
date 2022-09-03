import functools

def carPooling(trips, capacity: int) -> bool:
    modifiedTrips = []
        
    for trip in trips:
        modifiedTrips.append([trip[1], -trip[0]])
        modifiedTrips.append([trip[2], trip[0]])
            
        
    def compare(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        else:
            return a[0] - b[0]
        
    modifiedTrips = sorted(modifiedTrips, key = functools.cmp_to_key(compare))

    for trip in modifiedTrips:
        capacity += trip[1]
        if capacity < 0:
            return False
            
    return True

# [4, 3, 5], [2, 3, 5], [6, 4, 7], [4, 5, 6]
print(carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13))