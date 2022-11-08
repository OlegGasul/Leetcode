from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        
        letters = {
            'w': ('two', '2'),
            'u': ('four', '4'),
            'x': ('six', '6'),
            'f': ('five', '5'),
            'z': ('zero', '0'),
            'r': ('three', '3'),
            't': ('eight', '8'),
            's': ('seven', '7'),
            'i': ('nine', '9'),
            'n': ('one', '1')
        }
        
        result = []
        for ch, (word, digit) in letters.items():
            digitCount = counter[ch]
            result.append(digit * digitCount)
		    
            for c in word:
                counter[c] -= digitCount
	    
        return ''.join(sorted(result))

solution = Solution()
print(solution.originalDigits("owoztneoer"))
print(solution.originalDigits("fviefuro"))
print(solution.originalDigits("threefour"))