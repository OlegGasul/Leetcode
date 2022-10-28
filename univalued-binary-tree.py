class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isUnivalTree(root) -> bool:
    if not root:
        return False
        
    def dfs(node):
        if node.left and (node.val != node.left.val or not dfs(node.left)):
            return False
        
        if node.right and (node.val != node.right.val or not dfs(node.right)):
            return False
        
        return True
        
    return dfs(root)

print(isUnivalTree(TreeNode(1, None, TreeNode(1, TreeNode(1), TreeNode(1)))))
print(isUnivalTree(TreeNode(1, None, TreeNode(1, TreeNode(2), TreeNode(1)))))