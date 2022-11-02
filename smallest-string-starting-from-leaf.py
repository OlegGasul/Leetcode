class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root) -> str:
        a = ord('a')
        
        result = ""
        
        def dfs(node, value = ''):
            nonlocal result
            
            value = chr(a + node.val) + value
            
            if not node.left and not node.right:
                if not result:
                    result = value
                else:
                    result = min(result, value)
                return
            
            if node.left:
                dfs(node.left, value)
                
            if node.right:
                dfs(node.right, value)
        
        dfs(root)
        
        return result

solution = Solution()
print(solution.smallestFromLeaf(TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(5), TreeNode(6)))))