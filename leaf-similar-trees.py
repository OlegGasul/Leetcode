class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2) -> bool:

        def dfs(node, leafs):
            if not node.left and not node.right:
                leafs.append(node.val)
                return

            if node.left:
                dfs(node.left, leafs)
            if node.right:
                dfs(node.right, leafs)

        a = []
        dfs(root1, a)

        b = []
        dfs(root2, b)

        return a == b

solution = Solution()
assert solution.leafSimilar(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(5, TreeNode(2), TreeNode(3))) == True
assert solution.leafSimilar(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(5, TreeNode(2), TreeNode(1))) == False