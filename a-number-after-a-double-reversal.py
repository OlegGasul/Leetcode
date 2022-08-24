def isSameAfterReversals(num: int) -> bool:
    return num == 0 or num % 10 != 0

print(isSameAfterReversals(526))
print(isSameAfterReversals(5260))
print(isSameAfterReversals(0))