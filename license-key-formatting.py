def licenseKeyFormatting(s: str, k: int) -> str:
    word = ''.join(s.split('-'))
        
    result = []
    i = len(word)
        
    while i > 0:
        result.insert(0, word[max(i - k, 0) : i].upper())
        i -= k
            
    return '-'.join(result)

print(licenseKeyFormatting("5F3Z-2e-9-w", 4))
print(licenseKeyFormatting("2-5g-3-J", 2))