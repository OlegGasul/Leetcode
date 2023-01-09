class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        
        if not root:
            return result

        def dfs(node):
            result.append(node.val)
            
            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            
        
        dfs(root)

        return result

solution = Solution()
assert solution.preorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 2, 3]