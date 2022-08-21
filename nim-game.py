def canWinNim(n: int) -> bool:
    return bool(n % 4)

print(canWinNim(5))
print(canWinNim(16))