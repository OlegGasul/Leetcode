class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root) -> int:
    result = float('inf')
        
    def dfs(node, depth):
        nonlocal result
            
        if not node.left and not node.right:
            result = min(result, depth)
        else:
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)
                    
    if root: 
        dfs(root, 1)
            
    return result if result != float('inf') else 0

print(minDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))