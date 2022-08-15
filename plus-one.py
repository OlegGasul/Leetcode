def plusOne(digits):
    index = len(digits) - 1
    
    while index >= 0:
        digits[index] += 1
        if digits[index] <= 9:
            return digits
        digits[index] = 0
        index -= 1
    
    digits[0] = 0
    digits.insert(0, 1)

    return digits


# print(list(plusOne([1, 2, 2])))
# print(list(plusOne([1, 2, 9])))
# print(list(plusOne([9, 9, 9])))
# print(list(plusOne([8, 9, 9, 9])))
# print(list(plusOne([8, 9, 9, 8])))
print(list(plusOne([9])))
