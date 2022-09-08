def numOfBurgers(tomatoSlices: int, cheeseSlices: int):
    # 4x + 2y = 16
    # x + y = 7
        
    # x = 7 - y
    # 28 - 4y + 2y = 16
    # 2y = 28 - 16
    # 2y = 12
    # y = 6
    # y = 7 - 6

    if tomatoSlices % 2 == 1:
        return []
        
    jumbo = (4 * cheeseSlices - tomatoSlices) // 2
    small = cheeseSlices - jumbo

    if small <= 0 or jumbo <= 0:
        return []

    return [small, jumbo]

print(numOfBurgers(16, 7))
print(numOfBurgers(17, 4))
print(numOfBurgers(4, 17))