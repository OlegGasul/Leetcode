def minimumBuckets(street: str) -> int:
    street = list(street)
    street.insert(0, 'H')
    street.append('H')

    result = 0
        
    for i in range(1, len(street) - 1):
        if street[i] == 'H':
            if street[i - 1] == 'C':
                continue
                
            if street[i - 1] == 'H' and street[i + 1] == 'H':
                return -1
            
            if street[i + 1] == '.':
                street[i + 1] = 'C'
                result += 1
            elif street[i - 1] == '.':
                street[i - 1] = 'C'
                result += 1
                    
    return result

print(minimumBuckets("H..H"))
print(minimumBuckets(".H.H."))
print(minimumBuckets(".HHH."))