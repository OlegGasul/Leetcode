class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    result = 0
        
    def dfs(node, depth):
        nonlocal result
            
        result = max(result, depth)
        if node.left:
            dfs(node.left, depth + 1)
        if node.right:
            dfs(node.right, depth + 1)
                
    if root:
        dfs(root, 1)
        
    return result

print(maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))