class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root) -> str:
    if not root:
        return ""
        
    def printNode(node):
        result = str(node.val)
            
        if not node.left and node.right:
            result += "()"
            
        if node.left:
            result += "(" + printNode(node.left) + ")"
        if node.right:
            result += "(" + printNode(node.right) + ")"
                
        return result
        
    return printNode(root)

print(tree2str(TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))))
print(tree2str(TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))))