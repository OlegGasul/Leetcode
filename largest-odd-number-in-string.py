def largestOddNumber(num: str) -> str:
    for i in reversed(range(len(num))):
        if int(num[i]) % 2 == 1:
            return num[0 : i + 1]

    return ""

print(largestOddNumber("35427"))
print(largestOddNumber("4206"))
print(largestOddNumber("42016"))