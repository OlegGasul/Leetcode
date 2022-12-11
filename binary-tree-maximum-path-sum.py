class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        result = float('-inf')

        def calculateTotals(node):
            nonlocal result
            
            if not node:
                return 0

            sumFromLeft = max(calculateTotals(node.left), 0)
            sumFromRight = max(calculateTotals(node.right), 0)

            result = max(result, sumFromLeft + node.val + sumFromRight)

            return max(sumFromLeft + node.val, sumFromRight + node.val)

        calculateTotals(root)

        return result

solution = Solution()
assert solution.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 42
assert solution.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6