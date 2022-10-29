def numWaterBottles(numBottles: int, numExchange: int) -> int:
    if numExchange == 0:
        return numBottles
    
    result = 0
    empty = 0
        
    while numBottles:
        result += numBottles
        empty += numBottles
            
        numBottles = empty // numExchange
        empty = empty % numExchange
        
    return result

print(numWaterBottles(9, 3))
print(numWaterBottles(8, 3))
print(numWaterBottles(15, 4))
print(numWaterBottles(15, 0))
print(numWaterBottles(3, 0))