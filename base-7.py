def convertToBase7(num: int) -> str:
    if num == 0:
        return "0"
        
    sign = "-" if num < 0 else ""
    result = ""
    num = abs(num)
        
    while num:
        result = str(num % 7) + result
        num //= 7
            
    return sign + result

print(convertToBase7(100))
print(convertToBase7(7 * 10))
print(convertToBase7(-7))
print(convertToBase7(-6))
print(convertToBase7(0))