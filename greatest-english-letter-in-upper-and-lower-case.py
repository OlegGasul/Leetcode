def greatestLetter(s: str) -> str:
    lowers = set()
    uppers = set()
        
    greater = ''
        
    for ch in s:
        if ch.islower():
            if ch.upper() in uppers:
                greater = max(greater, ch.upper())
                    
            lowers.add(ch)
        else:
            if ch.lower() in lowers:
                greater = max(greater, ch.upper())
                
            uppers.add(ch)
                
    return greater

print(greatestLetter("arRAzFif"))
print(greatestLetter("AbCdEfGhIjK"))
print(greatestLetter("lEeTcOdE"))