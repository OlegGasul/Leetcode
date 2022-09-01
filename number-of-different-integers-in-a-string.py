def numDifferentIntegers(word: str) -> int:
    nums = set()
        
    digits = ""
        
    for ch in word:
        if ch.isdigit():
            digits += ch
        elif digits:
            nums.add(int(digits))
            digits = ""
                
    if digits:
        nums.add(int(digits))

    return len(nums)

print(numDifferentIntegers("a123bc34d8ef34"))
print(numDifferentIntegers("a1b01c001"))