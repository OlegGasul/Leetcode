from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root, to_delete):
        queue = deque([(root, None, None)])
        result = []

        while queue:
            node, parent, leftRight = queue.popleft()

            if node.val in to_delete:
                if parent:
                    if leftRight:
                        parent.right = None
                    else:
                        parent.left = None
                
                currentParent = None
            else:
                if not parent:
                    result.append(node)
                currentParent = node

            if node.right:
                queue.append((node.right, currentParent, True))
            if node.left:
                queue.append((node.left, currentParent, False))

        return result

solution = Solution()
solution.delNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), [3, 5])