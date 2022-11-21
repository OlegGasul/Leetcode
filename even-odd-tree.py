class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root) -> bool:
        if not root:
            return False

        level = 0

        queue = [root]

        while queue:
            newQueue = []
            
            prev = None
            
            temp = []

            for node in queue:
                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                else:
                    if node.val % 2 != 0:
                        return False
                
                if prev:
                    if level % 2 == 0:
                        if node.val <= prev:
                            return False
                    else:
                        if node.val >= prev:
                            return False

                prev = node.val

                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)

            queue = newQueue
            level += 1

        return True

solution = Solution()
print(solution.isEvenOddTree(TreeNode(1, TreeNode(10, TreeNode(3, TreeNode(12), TreeNode(8))), TreeNode(4, TreeNode(7, TreeNode(6)), TreeNode(9, None, TreeNode(2))))))