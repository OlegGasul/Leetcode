class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root):

        def dfs(node, collector):
            if not node.left and not node.right:
                collector.append(node.val)
                return True
            
            if node.left:
                if dfs(node.left, collector):
                    node.left = None
            
            if node.right:
                if dfs(node.right, collector):
                    node.right = None

            return False

        result = []
        while root.left or root.right:
            collector = []
            dfs(root, collector)
            result.append(collector)

        result.append([root.val])

        return result

solution = Solution()
assert solution.findLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [[4, 5, 3], [2], [1]]
