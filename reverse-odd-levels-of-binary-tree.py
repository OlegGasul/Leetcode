class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    queue = [root]

    while queue:
        nums = []
        newQueue = []

        for node in queue:
            nums.append(node.val)

            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
        
        print(nums)

        queue = newQueue
    
    print()

def reverseOddLevels(root):
    if not root:
        return None
        
    queue = [root]
        
    level = 0
        
    while queue:
        newQueue = []
            
        if level % 2 != 0:
            length = len(queue)
            for i in range(length // 2):
                queue[i].val, queue[length - i - 1].val = queue[length - i - 1].val, queue[i].val
                    
        for node in queue:
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
        level += 1
            
    return root

printTree(reverseOddLevels(TreeNode(2, TreeNode(3, TreeNode(8), TreeNode(13)), TreeNode(5, TreeNode(21), TreeNode(34)))))