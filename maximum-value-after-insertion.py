def maxValue(n: str, x: int) -> str:
    isNegative = n[0] == "-"
    
    for i in range(1 if isNegative else 0, len(n)):
        num = int(n[i])
        if (isNegative and x < num) or (not isNegative and x > num):
            return n[0:i] + str(x) + n[i:]

    return n + str(x)


print(maxValue("335566", 4))
print(maxValue("-334455", 4))