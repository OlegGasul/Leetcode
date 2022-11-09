class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k: int) -> bool:
        visited = set()

        def dfs(node):
            if abs(node.val - k) in visited:
                return True

            visited.add(node.val)

            if node.left:
                if dfs(node.left):
                    return True
            if node.right:
                if dfs(node.right):
                    return True

            return False

        return dfs(root)

solution = Solution()
print(solution.findTarget(TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))))