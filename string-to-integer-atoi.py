def myAtoi(s: str) -> int:
    is_negative = False
    digits_started = False
    result = 0

    for char in s:
        if char >= '0' and char <= '9':
            result = result * 10 + int(char)
            digits_started = True
        else:
            if digits_started:
                break
            elif char == '-':
                is_negative = True
                digits_started = True
            elif char == '+':
                digits_started = True
            elif char != ' ':
                return 0

    max_value = 2 ** 31 - 1
    min_value = -2 ** 31
        
    result = result if not is_negative else result * -1
        
    if result >= max_value:
        result = max_value
    if result <= min_value:
        result = min_value
            
    return result

print(myAtoi("+12"))
print(myAtoi("+-12"))
print(myAtoi("   12"))
print(myAtoi("   -12"))
print(myAtoi("-91283472332"))
