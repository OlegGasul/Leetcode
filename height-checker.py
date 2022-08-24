def heightChecker(heights) -> int:
    ordered = sorted(heights)
        
    result = 0
    for i in range(len(heights)):
        if heights[i] != ordered[i]:
            result += 1
                
    return result

print(heightChecker([1, 1, 4, 2, 1, 3]))