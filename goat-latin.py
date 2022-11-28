class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        words = sentence.split(' ')
        
        for i in range(len(words)):
            word = words[i]
            w = list(word)

            if not w[0].lower() in vowels:
                w.append(w.pop(0))
            
            w += ['m', 'a']
            w += ['a'] * (i + 1)

            words[i] = ''.join(w)
        
        return ' '.join(words)

solution = Solution()
assert solution.toGoatLatin("I speak Goat Latin") == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
assert solution.toGoatLatin("The quick brown fox jumped over the lazy dog") == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"