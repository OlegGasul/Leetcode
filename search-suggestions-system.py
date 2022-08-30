class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for char in word:
            node = current.children.get(char)
            if node == None:
                node = TrieNode()
                current.children.update({ char: node })
            current = node
            current.words.append(word)
            current.words.sort()

    def searchString(self, word, maxSize):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            currentNode = node
            if not currentNode:
                break

        return currentNode.words[0 : maxSize] if currentNode else []

class Solution:
    def suggestedProducts(self, products, searchWord: str):
        trie = Trie()

        for product in products:
            trie.insertString(product)
        
        result = []
        for i in range(len(searchWord)):
            result.append(trie.searchString(searchWord[0 : i + 1], 3))

        return result



solution = Solution()
print(solution.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print(solution.suggestedProducts(["havanna"], "mouse"))