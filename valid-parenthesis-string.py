def checkValidString(s: str) -> bool:
    left, right = 0, 0

    for char in s:
        if char == '(':
            right += 1
            left += 1
        elif char == ')':
            right -= 1
            left -= 1
        elif char == '*':
            right += 1
            left -= 1
        
        if right < 0:
            return False

        left = max(left, 0)

    return left == 0

print(checkValidString("((*)***"))