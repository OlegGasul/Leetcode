from collections import deque

class Trie:
    def __init__(self):
        self.isword = 0
        self.children = {}

class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        root = Trie()
        
        for word in words:
            node = root
            
            for char in word:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            
            node.isword += 1
        
        result = 0
        queue = deque([root])

        for char in s:
            length = len(queue)

            for _ in range(length):
                cur = queue.popleft()
                
                if cur.isword:
                    result += cur.isword
                    cur.isword = 0
                
                if char in cur.children:
                    queue.append(cur.children[char])
                    del cur.children[char]
                
                if cur.children:
                    queue.append(cur)
        
        while queue:
            cur = queue.pop()
            if cur.isword:
                result += cur.isword
        
        return result

solution = Solution()
print(solution.numMatchingSubseq("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))