from time import sleep

def addBinarySimple(a: str, b: str) -> str:
    return str(int(a, 2) + int(b, 2))[2:]

def addBinary(a: str, b: str) -> str:
    a = list(a)
    b = list(b)

    carry = 0
    result = []

    while a or b or carry == 1:
        bit1 = int(a.pop()) if a else 0
        bit2 = int(b.pop()) if b else 0
        
        value = bit1 ^ bit2 ^ carry
        carry = 1 if bit1 + bit2 + carry >= 2 else 0
        
        result.insert(0, value)

    return ''.join([str(x) for x in result])


print(addBinary("11", "1"))
print(addBinary("1111", "1111"))
print(addBinary("1010", "1011"))