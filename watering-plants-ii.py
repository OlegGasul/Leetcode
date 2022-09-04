def minimumRefill(plants, capacityA: int, capacityB: int) -> int:
    left = 0
    right = len(plants) - 1
        
    alice = capacityA
    bob = capacityB
        
    aliceRefills = 0
    bobRefills = 0
        
    while left < right:
        if alice < plants[left]:
            aliceRefills += 1
            alice = capacityA
                
        alice -= plants[left]
        left += 1
            
        if bob < plants[right]:
            bobRefills += 1
            bob = capacityB
                
        bob -= plants[right]
            
        right -= 1
            
    if left == right:
        if alice >= bob:
            if alice < plants[left]:
                aliceRefills += 1
        else:
            if bob < plants[right]:
                bobRefills += 1
        
    return aliceRefills + bobRefills

print(minimumRefill([2, 2, 3, 3], 5, 5))
print(minimumRefill([2, 2, 3, 3], 3, 4))
print(minimumRefill([5], 10, 8))