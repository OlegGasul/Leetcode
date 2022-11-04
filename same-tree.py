class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q) -> bool:
        
        def dfs(node1, node2):
            if (node1 and not node2) or (not node1 and node2):
                return False
            
            if node1.val != node2.val:
                return False
            
            if (node1.left and not node2.left) or (not node1.left and node2.left):
                return False
            
            if (node1.right and not node2.right) or (not node1.right and node2.right):
                return False
            
            if node1.left and node2.left:
                if not dfs(node1.left, node2.left):
                    return False
                
            if node1.right and node2.right:
                if not dfs(node1.right, node2.right):
                    return False
                
            return True
        
        if not p and not q:
            return True
        
        return dfs(p, q)

solution = Solution()
print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
print(solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, None, TreeNode(3))))
print(solution.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))