morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def uniqueMorseRepresentations(words) -> int:
    a = ord('a')
    
    transformed = []
    for word in words:
        word = list(word)
        for i in range(len(word)):
            word[i] = morse[ord(word[i]) - a]
        transformed.append(''.join(word))

    return len(set(transformed))


print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))