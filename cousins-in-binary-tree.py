class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root, x: int, y: int) -> bool:
        queue = [(root, None)]

        while queue:
            newQueue = []

            xParent = None
            yParent = None

            for node, parent in queue:
                if node.val == x:
                    xParent = parent
                elif node.val == y:
                    yParent = parent

                if node.left:
                    newQueue.append((node.left, node))
                if node.right:
                    newQueue.append((node.right, node))

            if xParent and yParent:
                return xParent != yParent

            queue = newQueue

        return False

solution = Solution()
print(solution.isCousins(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 4, 3))
print(solution.isCousins(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5))), 5, 4))