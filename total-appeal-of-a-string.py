def appealSum(s: str) -> int:
    last = {}
    current = 0
    result = 0
    
    for i, ch in enumerate(s):
        current += i - (last[ch] if ch in last else -1)
        last[ch] = i
        result += current
    
    return result

print(appealSum("abbca"))
print(appealSum("codecodecodecodecodecodecodecodecodecodecodecodecodecodecodecodecode"))