class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        
        result = 0
        
        def dfs(node, isLeft = False):
            nonlocal result
            if isLeft and not node.left and not node.right:
                result += node.val
                return
            
            if node.left:
                dfs(node.left, True)
            
            if node.right:
                dfs(node.right)

        dfs(root)

        return result

solution = Solution()
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(solution.sumOfLeftLeaves(root))

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(solution.sumOfLeftLeaves(root))