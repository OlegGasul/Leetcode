class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root, target: int):
        def dfs(node):
            if node.left:
                if dfs(node.left):
                    node.left = None
            if node.right:
                if dfs(node.right):
                    node.right = None
                    
            return not node.left and not node.right and node.val == target
        
        if dfs(root):
            return None
        
        return root

solution = Solution()
solution.removeLeafNodes(TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(3, TreeNode(2), TreeNode(4))), 3)