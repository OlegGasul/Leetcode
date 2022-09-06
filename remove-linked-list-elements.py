class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printNodes(head):
    nums = []

    while head:
        nums.append(head.val)
        head = head.next

    print(nums)

def removeElements(head, val: int):
    temp = ListNode(0, head)
        
    prev = temp
    node = head
        
    while node:
        if node.val == val:
            prev.next = node.next
        else:
            prev = node
            
        node = node.next
            
    return temp.next

printNodes(removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 6))
printNodes(removeElements(ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))), 1))