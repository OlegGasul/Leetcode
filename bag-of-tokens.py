def bagOfTokensScore(tokens, power: int) -> int:
    tokens.sort()
    
    maxScore = 0
    score = 0
    
    while tokens:
        if tokens[0] <= power:
            power -= tokens.pop(0)
            score += 1
            maxScore = max(maxScore, score)
        elif score > 0:
            power += tokens.pop(-1)
            score -= 1
        else:
            break
    
    return maxScore

print(bagOfTokensScore([100, 200, 300, 400], 200))