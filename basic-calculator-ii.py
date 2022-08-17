def calculate(s: str):
    stack = []
    length = len(s)

    i = 0
    prevSign = "+"
    
    while i < length:
        if s[i].isdigit():
            left = i
            while i + 1 < length and s[i + 1].isdigit():
                i += 1
            num = int(s[left : i + 1])
        
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
            if prevSign == "+":
                stack.append(num)
            elif prevSign == "-":
                stack.append(-num)
            elif prevSign == "*":
                stack.append(num * stack.pop())
            elif prevSign == "/":
                val = stack.pop()
                result = abs(val) // abs(num)
                if val < 0:
                    result *= -1
                
                stack.append(result)

            prevSign = s[i]
        
        i += 1

    return sum(stack)
    

print(calculate("1 + 10 / 2 + 1 * 4 + 2 * 5"))
print(calculate("3 / 2 + 10"))
print(calculate("14 - 3 / 2"))