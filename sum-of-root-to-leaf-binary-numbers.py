class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sumRootToLeaf(root) -> int:
    result = 0
        
    def dfs(node, value):
        nonlocal result
            
        node.val += value << 1
            
        if not node.left and not node.right:
            result += node.val
        else:
            if node.left:
                dfs(node.left, node.val)
            if node.right:
                dfs(node.right, node.val)
                    
    dfs(root, 0)
        
    return result

print(sumRootToLeaf(TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)))))