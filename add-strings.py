def addStrings(num1: str, num2: str) -> str:
    num1 = list(num1)
    num2 = list(num2)

    result = []
    rest = 0

    while num1 or num2 or rest:
        value = (int(num1.pop()) if num1 else 0) + (int(num2.pop()) if num2 else 0) + rest

        result.insert(0, str(value % 10))
        rest = value // 10

    while num1 or rest:
        value = (int(num1.pop()) if num1 else 0) + rest
        result.insert(0, str(value % 10))
        rest = value // 10

    return ''.join(result)
    

print(addStrings("11", "123"))
print(addStrings("123", "11"))
print(addStrings("123", "17"))
print(addStrings("999", "1"))
print(addStrings("999", "99999"))
print(addStrings("9999999", "1"))