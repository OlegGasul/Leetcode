def maximumEvenSplit(finalSum: int):
    if finalSum % 2 == 1:
        return []

    subtractBy = 2
    visitSet = set()
        
    while finalSum > 0:
        if (finalSum - subtractBy == subtractBy or 
            finalSum - subtractBy in visitSet):
            visitSet.add(finalSum)
            return list(visitSet)
        
        visitSet.add(subtractBy)
        finalSum -= subtractBy
        subtractBy += 2
    
    return list(visitSet)

    
# 28
# 28 - 2 - 4 = 22
# 22 - 6 = 16
# 2, 4, 6, 16
# print(maximumEvenSplit(28))

print(maximumEvenSplit(20000))

# 16 - 2 = 14
# 14 - 6 = 8
# 8 - 8 = 0
# print(maximumEvenSplit(16))