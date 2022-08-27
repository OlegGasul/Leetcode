def maximumTime(time: str) -> str:
    parts = list(time)
    
    if parts[0] == "?":
        if parts[1] == "?":
            parts[0] = "2"
        else:
            hour = int(parts[1])
            if hour < 4:
                parts[0] = "2"
            else:
                parts[0] = "1"
    
    if parts[1] == "?":
        hour = int(parts[0])
        if hour < 2:
            parts[1] = "9"
        else:
            parts[1] = "3"

    if parts[3] == "?":
        parts[3] = "5"
    if parts[4] == "?":
        parts[4] = "9"

    return ''.join(parts)

    
print(maximumTime("?3:?0"))
print(maximumTime("2?:?0"))
print(maximumTime("0?:3?"))
print(maximumTime("1?:22"))
print(maximumTime("?4:03"))
print(maximumTime("?3:02"))