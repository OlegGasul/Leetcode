def toHex(num: int) -> str:
    if num == 0:
        return "0"
    if num < 0:
        num += 16 ** 8
    
    hexes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    
    result = ""
    while num:
        result = hexes[num % 16] + result
        num //= 16

    return result


print(toHex(26))
print(toHex(21116))
print(toHex(1))
print(toHex(0))
print(toHex(-1))
print(toHex(-2))