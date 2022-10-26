def decodeMessage(key: str, message: str) -> str:
    letter = ord('a')
    mappings = {}
        
    for ch in key:
        if ch == ' ' or ch in mappings:
            continue
            
        mappings[ch] = chr(letter)
        letter += 1
    
    return ''.join([mappings[ch] if ch in mappings else ch for ch in message])

print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))