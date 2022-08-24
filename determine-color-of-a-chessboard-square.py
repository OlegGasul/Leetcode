def squareIsWhite(coordinates: str) -> bool:
    return bool((ord(coordinates[0]) - ord("a") + 1 + int(coordinates[1])) % 2)

print(squareIsWhite("a1"))
print(squareIsWhite("h3"))