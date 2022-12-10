class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root) -> int:
        subTreeSums = []

        def dfs(node):
            if not node:
                return 0
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            total = leftSum + node.val + rightSum

            subTreeSums.append(total)

            return total
        
        total = dfs(root)
        result = 0

        for subTreeSum in subTreeSums:
            result = max(result, subTreeSum * (total - subTreeSum))
        
        return result % (10 ** 9 + 7)

solution = Solution()
solution.maxProduct(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))))