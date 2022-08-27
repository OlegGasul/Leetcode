class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printNodes(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)


def deleteDuplicates(head):
    prev = None
    node = head

    while node:
        if prev and prev.val == node.val:
            prev.next = node.next
        else:
            prev = node
        
        node = node.next
    
    return head


printNodes(deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))))