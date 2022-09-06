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

def deleteNode(node):
    nextNode = node.next
    nextVal = nextNode.val
        
    node.val = nextVal
    node.next = nextNode.next
    del nextNode

node = ListNode(5, ListNode(1, ListNode(9)))
head = ListNode(4, node)
deleteNode(node)
printNodes(head)
