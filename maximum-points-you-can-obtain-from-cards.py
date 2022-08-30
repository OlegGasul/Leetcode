def maxScore(cardPoints, k: int) -> int:
    if k <= 0:
        return 0
    
    length = len(cardPoints)
    total = sum(cardPoints)
    
    if k == length:
        return total

    if k == 1:
        return min(cardPoints[0], cardPoints[-1])

    window = 0
    size = length - k
    for i in range(size):
        window += cardPoints[i]

    i += 1
    result = total - window

    while i < length:
        window += cardPoints[i]
        window -= cardPoints[i - size]
        
        result = max(result, total - window)
        i += 1

    return result


print(maxScore([1, 2, 3, 4, 5, 6, 1], 3))
print(maxScore([100, 40, 17, 9, 73, 75], 3))
print(maxScore([1, 1000, 1], 1))
print(maxScore([1, 79, 80, 1, 1, 1, 200, 1], 3))
print(maxScore([1, 79, 80, 1, 1, 1, 200, 1], 0))
print(maxScore([1, 79, 80, 1, 1, 1, 200, 1], -10))