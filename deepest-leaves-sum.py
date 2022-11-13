class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root) -> int:
        if not root:
            return 0
        
        queue = [root]

        while queue:
            newQueue = []

            result = 0

            for node in queue:
                result += node.val
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)

            if not newQueue:
                return result

            queue = newQueue
        
        return 0

solution = Solution()
print(solution.deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)), TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))