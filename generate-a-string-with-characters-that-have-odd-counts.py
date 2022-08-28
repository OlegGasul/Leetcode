def generateTheString(n: int) -> str:
    if n == 0:
        return ''
    
    if n % 2 == 0:
        return 'a' * (n - 1) + 'b'
    else:
        return 'a' * n

print(generateTheString(10))
print(generateTheString(0))
print(generateTheString(3))
print(generateTheString(1))