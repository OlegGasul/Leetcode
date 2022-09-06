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

def deleteMiddle(head):
    node = head
        
    nodes = []
    while node:
        nodes.append(node)
        node = node.next
        
    length = len(nodes)
    if length == 1:
        return None
        
    index = length // 2
    nodes[index - 1].next = nodes[index].next
        
    return head

printNodes(deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
printNodes(deleteMiddle(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
printNodes(deleteMiddle(ListNode(2, ListNode(1))))