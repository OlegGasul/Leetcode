class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root, target: float) -> int:
        if not root:
            return None
        
        closest = None
        diff = float('inf')

        def dfs(node):
            nonlocal diff
            nonlocal closest

            if abs(node.val - target) < diff:
                closest = node.val
                diff = abs(node.val - target)
            
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        return closest
    
solution = Solution()
print(solution.closestValue(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5)), 3.714286))