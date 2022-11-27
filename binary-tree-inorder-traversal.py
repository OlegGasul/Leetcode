class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        if not root:
            return result

        def dfs(node):
            nonlocal result

            if node.left:
                dfs(node.left)
            
            result.append(node.val)
            
            if node.right:
                dfs(node.right)

        dfs(root)
        
        return result

solution = Solution()
assert solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))) == [1, 3, 2]
assert solution.inorderTraversal(None) == []
assert solution.inorderTraversal(TreeNode(1)) == [1]