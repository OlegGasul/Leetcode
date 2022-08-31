from collections import Counter
import string
import re

def mostCommonWord(paragraph: str, banned) -> str:
    paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
    paragraph = paragraph.strip()
    paragraph = re.split(r'\s+', paragraph)
    
    counter = Counter(paragraph)

    banned = set(banned)

    for pair in counter.most_common():
        if pair[0] in banned:
            continue
        return pair[0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
print(mostCommonWord("..Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))