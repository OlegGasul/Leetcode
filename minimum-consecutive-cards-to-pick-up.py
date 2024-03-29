def minimumCardPickup(cards) -> int:
    indecies = {}
    
    result = float('inf')
        
    for i in range(len(cards)):
        if cards[i] in indecies:
            result = min(result, i - indecies[cards[i]])
            
        indecies[cards[i]] = i

    return result + 1 if result != float('inf') else -1

print(minimumCardPickup([3, 4, 2, 3, 4, 7]))