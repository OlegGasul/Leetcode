def timeRequiredToBuy(tickets, k: int) -> int:
    result = 0
        
    while tickets:
        i = 0
        while i < len(tickets):
            tickets[i] -= 1
            result += 1
                
            if tickets[i] == 0:
                tickets.pop(i)
                    
                if i == k:
                    return result
                    
                if i < k:
                    k -= 1
            else:
                i += 1
            
    return result

print(timeRequiredToBuy([2, 3, 2], 2))
print(timeRequiredToBuy([5, 1, 1, 1], 0))