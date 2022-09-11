from collections import Counter

def countBalls(lowLimit: int, highLimit: int) -> int:
    ballCounts = Counter()
        
    for ballNumber in range(lowLimit, highLimit + 1):
        ballCounts[sum([int(x) for x in list(str(ballNumber))])] += 1
            
    return ballCounts.most_common()[0][1]

print(countBalls(1, 10))
print(countBalls(5, 15))
print(countBalls(19, 28))
print(countBalls(1, 12800))