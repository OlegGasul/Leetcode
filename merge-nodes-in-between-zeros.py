class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def printNodes(head):
    while head:
        print(head.val)
        head = head.next

def mergeNodes(head):
    item = head

    start = None
    prev = head
    sum = 0

    while item:
        if item.val == 0:
            if start:
                node = ListNode(sum)
                start.next = node
                node.next = item.next
                item = node
                start = node
            else:
                start = prev
            sum = 0
        else:
            sum += item.val

        prev = item
        item = item.next

    return head.next

head = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
printNodes(mergeNodes(head))