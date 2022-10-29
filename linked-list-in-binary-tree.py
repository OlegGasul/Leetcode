class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSubPath(head, root) -> bool:

    def dfs(treeNode, listNode):
        if treeNode.val == listNode.val:
            if listNode.next == None:
                return True
                
            if not treeNode.left and not treeNode.right:
                return False
                
            if treeNode.left:
                result = dfs(treeNode.left, listNode.next)
                if result:
                    return True
                    
            if treeNode.right:
                result = dfs(treeNode.right, listNode.next)
                if result:
                    return True
                
        return False
        
    queue = [root]
        
    while queue:
        newQueue = []
            
        for node in queue:
            if dfs(node, head):
                return True
                
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
                    
        queue = newQueue
            
    return False

print(isSubPath(
    ListNode(4, ListNode(2, ListNode(8))),
    TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1))), TreeNode(4, TreeNode(2, TreeNode(6), TreeNode(8, TreeNode(1), TreeNode(3)))))
))