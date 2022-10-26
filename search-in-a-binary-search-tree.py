class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val: int):
    if not root:
        return None
        
    def dfs(node):
        nonlocal val
            
        if node.val == val:
            return node
            
        if node.val > val:
            if node.left:
                return dfs(node.left)
            else:
                return None
        elif node.val < val:
            if node.right:
                return dfs(node.right)
            else:
                return None
                
    return dfs(root)

print(searchBST(TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2))