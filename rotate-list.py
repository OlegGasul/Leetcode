class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printNodes(head):
    item = head
    while item != None:
        print(item.val)
        item = item.next

def rotateRight(head, k: int):
    items = []
    item = head
    while item != None:
        items.append(item)
        item = item.next
    
    length = len(items)

    if length == 0:
        return head
    
    perm = k % length
    if perm == 0:
        return head

    items[length - perm - 1].next = None
    items[length - 1].next = head

    return items[length - perm]


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newHead = rotateRight(head, 24)
printNodes(newHead)