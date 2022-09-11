def convertTime(current: str, correct: str) -> int:
    current = current.split(':')
    correct = correct.split(':')
        
    current = int(current[0]) * 60 + int(current[1])
    correct = int(correct[0]) * 60 + int(correct[1])
        
    if current == correct:
        return 0
        
    result = 0
        
    if current < correct:
        diff = correct - current
    else:
        diff = 24 * 60 - current + correct
            
    while diff:
        if diff >= 60:
            result += diff // 60
            diff = diff % 60
        elif diff >= 15:
            result += diff // 15
            diff = diff % 15
        elif diff >= 5:
            result += diff // 5
            diff = diff % 5
        else:
            result += diff
            diff = 0
            
    return result

print(convertTime("02:30", "04:35"))
print(convertTime("11:00", "11:01"))
print(convertTime("21:30", "11:01"))