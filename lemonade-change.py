def lemonadeChange(bills) -> bool:
    fives = 0
    tens = 0
        
    for b in bills:
        if b == 5:
            fives += 1
        elif b == 10:
            if not fives:
                return False
            fives -= 1
            tens += 1
        elif b == 20:
            if not fives and not tens:
                return False
                
            if fives and tens:
                fives -= 1
                tens -= 1
            elif fives:
                if fives < 3:
                    return False
                fives -= 3
            else:
                return False
                    
    return True

print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 10, 20]))