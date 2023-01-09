class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        result = []
        if not root:
            return result

        def dfs(node):
            result.append(node.val)

            if node.children:
                for c in node.children:
                    dfs(c)
        
        dfs(root)
        
        return result

solution = Solution()
assert solution.preorder(Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])) == [1, 3, 5, 6, 2, 4]