import bisect

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root: TreeNode) -> TreeNode:
    if not root:
        return None
        
    nums = []
        
    queue = [root]
        
    while queue:
        newQueue = []
            
        for node in queue:
            bisect.insort_left(nums, node.val)
                
            if node.left:
                newQueue.append(node.left)
                
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
            
    result = TreeNode(nums.pop(0))
    node = result

    while nums:
        node.right = TreeNode(nums.pop(0))
        node = node.right
            
    return result

print(increasingBST(TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))))