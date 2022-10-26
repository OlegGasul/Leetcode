class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val: int):
    if not root:
        return TreeNode(val)
        
    def dfs(node):
        nonlocal val
            
        if val > node.val:
            if not node.right:
                node.right = TreeNode(val)
                return
            else:
                return dfs(node.right)
        elif val < node.val:
            if not node.left:
                node.left = TreeNode(val)
                return
            else:
                return dfs(node.left)
                
    dfs(root)
        
    return root

print(insertIntoBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5))