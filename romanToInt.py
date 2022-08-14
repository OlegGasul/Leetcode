# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

def romanToInt(s: str) -> int:
    result = 0
    
    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    prev = None
    for char in s:
        result += roman_to_int[char]
        
        if prev == 'I':
            if char in ['V', 'X']:
                result -= 2
        if prev == 'X':
            if char in ['L', 'C']:
                result -= 20
        if prev == 'C':
            if char in ['D', 'M']:
                result -= 200

        prev = char

    return result

print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))