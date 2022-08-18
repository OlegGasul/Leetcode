def brokenCalc(startValue: int, target: int) -> int:
    count = 0

    while startValue < target:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1

        count += 1

    return count + (startValue - target)

print(brokenCalc(5, 8))