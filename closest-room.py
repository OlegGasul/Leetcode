import functools

def closestRoom(rooms, queries):
    length = len(rooms)

    def compare(a, b):
        return a[1] - b[1]
    
    rooms = sorted(rooms, key = functools.cmp_to_key(compare))

    dp = {}
    ids = []

    for i in reversed(range(len(rooms))):
        ids.append(rooms[i][0])

        dp[i] = sorted(ids)

    def findRoomIndexWithSizeAtLeast(size):
        if size > rooms[-1][1]:
            return -1
        
        left = 0
        right = len(rooms) - 1

        while left < right:
            middle = left + (right - left) // 2
            value = rooms[middle][1]

            if value < size:
                left = middle + 1
            else:
                right = middle

        return left

    def findClosestId(index, id):
        ids = dp[index]
        
        if len(ids) == 1:
            return ids[0]

        left = 0
        right = len(ids) - 1

        while right - left > 1:
            middle = left + (right - left) // 2
            value = ids[middle]

            if value == id:
                return value

            if value < id:
                left = middle + 1
            else:
                right = middle

        abs1 = abs(id - ids[left])
        abs2 = abs(id - ids[right])

        if abs1 == abs2:
            return min(ids[left], ids[right])
        elif abs1 < abs2:
            return ids[left]
        else:
            return ids[right]
    
    for i in range(len(queries)):
        index = findRoomIndexWithSizeAtLeast(queries[i][1])
        if index >= 0:
            queries[i] = findClosestId(index, queries[i][0])
        else:
            queries[i] = -1

    return queries


print(closestRoom([[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]]))
print(closestRoom([[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], [[2, 3], [2, 4], [2, 5]]))