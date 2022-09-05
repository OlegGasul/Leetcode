def canSeePersonsCount(heights):
    length = len(heights)
        
    stack = []
    result = [0] * length
        
    for i in reversed(range(length)):
        visible = 0
        while stack and heights[i] > stack[-1]:
            stack.pop()
            visible += 1

        if stack:
            visible += 1
        
        stack.append(heights[i])
        result[i] = visible
            
    return result

print(canSeePersonsCount([10, 6, 8, 5, 11, 9]))