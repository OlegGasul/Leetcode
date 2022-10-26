class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def binaryTreePaths(root):
    if not root:
        return ""
        
    result = []
        
    def dfs(node, values):
        nonlocal result
            
        values = values + [str(node.val)]
            
        if not node.left and not node.right:
            result.append('->'.join(values))
        else:
            if node.left:
                dfs(node.left, values)
            if node.right:
                dfs(node.right, values)
                    
    dfs(root, [])
        
    return result

print(binaryTreePaths(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))))
print(binaryTreePaths(TreeNode(1)))