def numRescueBoats(people, limit):
    people = sorted(people, reverse = True)
    
    if people[0] > limit:
        return -1

    left = 0
    right = len(people) - 1
    result = 0
    
    while len(people) > 1:
        boat = limit

        if boat >= people[0]:
            boat -= people[0]
            people.pop(0)
        
        if boat >= people[0]:
            boat -= people[0]
            people.pop(0)
        elif boat >= people[-1]:
            boat -= people[-1]
            people.pop()

        result += 1

    return result + len(people)

    




print(numRescueBoats([3, 2, 2, 1], 3))
# print(numRescueBoats([3, 5, 3, 4], 5))
# print(numRescueBoats([1, 2], 3))

# 3, 3, 2, 2, 2
print(numRescueBoats([3, 2, 3, 2, 2], 6))

