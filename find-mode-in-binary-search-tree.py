from collections import Counter

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findMode(root):
    if not root:
        return []
        
    counter = Counter()
        
    queue = [root]
        
    while queue:
        newQueue = []
            
        for node in queue:
            counter[node.val] += 1
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
            
        queue = newQueue
            
    mostCommon = counter.most_common()
    element, maxCount = mostCommon.pop(0)
    result = [element]
        
    while mostCommon:
        element, count = mostCommon.pop(0)
        if count < maxCount:
            break
        result.append(element)
            
    return result

print(findMode(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(3), TreeNode(7)))))