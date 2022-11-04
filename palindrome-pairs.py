class Solution:
    def palindromePairs(self, words):
        # keep a hashmap of word to its index
        idx_map = {}
        for i, word in enumerate(words):
            idx_map[word] = i
            
        result = set()
        
        for i, word in enumerate(words):
            if not word:
                # we don't process empty string by itself
                continue
            
            # generate all possible LHS that would form
            # a palindrome with current word
            for j in range(len(word)):
                current = word[:j]
                target = word[j:][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    result.add((idx_map[target], i))
                    
            # generate all possible RHS that would form
            # a palindrome with current word
            for j in range(len(word), -1, -1):
                current = word[j:]
                target = word[:j][::-1]
                if current == current[::-1] and target != word and target in idx_map:
                    result.add((i, idx_map[target]))
                    
            # check if current word is already a palindrome and
            # if we have an empty string in our map
            if word == word[::-1] and "" in idx_map:
                idx = idx_map[""]
                result.add((i, idx))
                result.add((idx, i))

        return list(result)

solution = Solution()
print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))