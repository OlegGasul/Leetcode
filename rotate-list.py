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
    count = 0

    item = head
    while item != None:
        count += 1
        last = item
        item = item.next

    if count == 0:
        return head
    
    perm = k % count
    if perm == 0:
        return head

    item = head
    prev = None
    for n in range(0, count - perm):
        prev = item
        item = item.next

    prev.next = None
    last.next = head

    return item


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newHead = rotateRight(head, 15)
printNodes(newHead)