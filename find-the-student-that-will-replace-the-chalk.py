def chalkReplacer(chalk, k: int) -> int:
    rest = k % sum(chalk)
    
    for i in range(len(chalk)):
        rest -= chalk[i]
        
        if rest < 0:
            return i
            
    return -1

print(chalkReplacer([5, 1, 5], 22))