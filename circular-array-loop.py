def circularArrayLoop(nums) -> bool:
    length = len(nums)

    def calculateIndex(current):
        value = current + nums[current]
        if abs(value) > length:
            value %= length
        
        if value >= length:
            value = value - length
        elif value < 0:
            value = length + value

        return value

    def isSameSign(val1, val2):
        return (val1 > 0 and val2 > 0) or (val1 < 0 and val2 < 0)

    for i in range(length):
        index = i
        visited = set()

        while not index in visited:
            newIndex = calculateIndex(index)

            if newIndex in visited:
                break
            visited.add(newIndex)

            if not isSameSign(nums[i], nums[newIndex]):
                break

            if newIndex == i:
                if len(visited) > 1:
                    return True
                else:
                    break
            
            index = newIndex
            

    return False


print(circularArrayLoop([2, -1, 1, 2, 2]))
print(circularArrayLoop([2, -1, 1, -2, -2]))
print(circularArrayLoop([-1, -1, -3]))
print(circularArrayLoop([-1, 2]))
print(circularArrayLoop([-2, -3, -9]))
print(circularArrayLoop([7, -1, 6, 7, 7]))