class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum: int):
        if not root:
            return []
        
        result = []

        def dfs(node, path, total):
            if not node.left and not node.right:
                if total + node.val == targetSum:
                    result.append(path + [node.val])
                return
            
            if node.left:
                dfs(node.left, path + [node.val], total + node.val)
            
            if node.right:
                dfs(node.right, path + [node.val], total + node.val)
            
        dfs(root, [], 0)
        
        return result

solution = Solution()
assert solution.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))), 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]