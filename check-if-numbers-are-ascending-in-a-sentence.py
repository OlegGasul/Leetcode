def areNumbersAscending(s: str) -> bool:
    prev = -1
        
    nums = ""
    for i in range(len(s)):
        if s[i].isnumeric():
            nums += s[i]
        else:
            if nums:
                num = int(nums)
                if num <= prev:
                    return False
                prev = num
                nums = ""
                    
                    
    if nums:
        num = int(nums)
        if num <= prev:
            return False
            
    return True

print(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(areNumbersAscending("hello world 5 x 5"))
print(areNumbersAscending("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))