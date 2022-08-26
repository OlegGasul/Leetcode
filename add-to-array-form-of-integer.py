def addToArrayForm(num, k: int):
    length = len(num)
    if length == 0:
        num = [0]
        length = 1
    
    i = length - 1
    rest = 0

    while k > 0 or rest > 0:
        value = num[i] + k % 10 + rest
        rest = value // 10
        
        num[i] = value % 10

        k //= 10

        if i > 0:
            i -= 1
        elif rest > 0 or k > 0:
            num.insert(0, 0)

    
    return num

print(addToArrayForm([2, 1, 5], 806))
print(addToArrayForm([2, 4, 7], 181))
print(addToArrayForm([1, 2, 0, 0], 34))
print(addToArrayForm([9, 9, 9], 1))
print(addToArrayForm([0], 23))
print(addToArrayForm([2, 4, 7, 9, 9, 0, 9], 11111222181))