def countPoints(rings: str) -> int:
    dp = [0] * 10
    colors = {
        "R": int('001', 2), "G": int('010', 2), "B": int('100', 2)
    }
        
    for i in range(0, len(rings), 2):
        dp[int(rings[i + 1])] |= colors[rings[i]]

    result = 0
    for i in range(10):
        result += 1 if dp[i] == 7 else 0
    
    # print(dp)

    return result

print(countPoints("B0B6G0R6R0R6G9"))