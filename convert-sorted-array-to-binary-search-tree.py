class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def createNode(start, end):
        middle = start + (end - start) // 2
        node = TreeNode(nums[middle])
            
        if middle > start:
            node.left = createNode(start, middle - 1)
                
        if middle < end:
            node.right = createNode(middle + 1, end)
            
        return node
        
    return createNode(0, len(nums) - 1)

print(sortedArrayToBST([-10, -3, 0, 5, 9]))