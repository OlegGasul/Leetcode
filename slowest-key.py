import functools

def slowestKey(releaseTimes, keysPressed: str) -> str:
    durations = {}
    releaseTimes.append(0)
        
    for i in range(len(keysPressed)):
        current = releaseTimes[i] - releaseTimes[i - 1]
        if not keysPressed[i] in durations:
            durations[keysPressed[i]] = current
        else:
            durations[keysPressed[i]] = max(durations[keysPressed[i]], current)

    def compare(a, b):
        if a[1] == b[1]:
            return ord(b[0]) - ord(a[0])
        else:
            return b[1] - a[1]

    return sorted(durations.items(), key = functools.cmp_to_key(compare))[0][0] if durations else ""

print(slowestKey([9, 29, 49, 50], "cbcd"))
print(slowestKey([12, 23, 36, 46, 62], "spuda"))