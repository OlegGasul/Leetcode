class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(head):
    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next
        
    def createNode(start, end):
        middle = start + (end - start) // 2
        node = TreeNode(nums[middle])
            
        if middle > start:
            node.left = createNode(start, middle - 1)
                
        if middle < end:
            node.right = createNode(middle + 1, end)
            
        return node
        
    if len(nums) == 0:
        return None
        
    return createNode(0, len(nums) - 1)

print(sortedListToBST(ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))))