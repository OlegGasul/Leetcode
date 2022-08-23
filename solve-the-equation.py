def solvePart(part):
    x = 0
    sign = 1
    num = ""
    value = 0

    for char in part:
        if char == '+':
            if num:
                value += int(num) * sign
                num = ""
            sign = 1
        elif char == '-':
            if num:
                value += int(num) * sign
                num = ""
            sign = -1
        elif char == 'x':
            x += (int(num) if num else 1) * sign
            num = ""
        elif char.isdigit():
            num += char
    if num:
        value += int(num) * sign
    
    return (x, value)


def solveEquation(equation: str) -> str:
    parts = equation.split('=')
    left = solvePart(parts[0])
    right = solvePart(parts[1])

    print(left)
    print(right)

    if left[0] - right[0] == 0:
        return "Infinite solutions"
    
    if left[1] == 0 and right[1] == 0:
        if left[0] == right[0]:
            return "Infinite solutions"
        else:
            return "x=0"

    return "x=" + str((right[1] - left[1]) // (left[0] - right[0]))



# print(solveEquation("x+5-3+x=6+x-2"))
# print(solveEquation("x=x"))
# print(solveEquation("2x=x"))
# print(solveEquation("2x+3x-6x=x+2"))
print(solveEquation("x=x+2"))