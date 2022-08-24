def largestGoodInteger(num: str) -> str:
    maximum = -1
    i = 0
    
    while i < len(num) - 1:
        if num[i] == num[i - 1]:
            if num[i] == num[i + 1]:
                maximum = max(maximum, int(num[i]))
            i += 2
        else:
            i += 1

    return str(maximum) * 3 if maximum >= 0 else ""

print(largestGoodInteger("6777133339"))
print(largestGoodInteger("677713333999"))
print(largestGoodInteger("2300019"))
