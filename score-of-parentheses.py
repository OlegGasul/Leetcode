def scoreOfParentheses(s: str) -> int:
    stack = [0]
        
    for char in s:
        if char == '(':
            stack.append(0)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b + max(2 * a, 1))

    return stack.pop()

print(scoreOfParentheses('(())(())'))