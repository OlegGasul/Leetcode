def truncateSentence(s: str, k: int) -> str:
    return ' '.join(s.split(' ')[0 : k])

print(truncateSentence("Hello how are you Contestant", 4))
print(truncateSentence("What is the solution to this problem", 4))