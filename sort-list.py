import bisect

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def printList(head):
    node = head
    result = []

    while node:
        result.append(node.val)
        node = node.next
    
    print(result)

def sortList(head):
    values = []
    nodes = []
        
    node = head
        
    while node:
        index = bisect.bisect_left(values, node.val)
        values.insert(index, node.val)
        nodes.insert(index, node)
            
        node = node.next
            
    if not nodes:
        return None
            
    for i in range(1, len(nodes)):
        nodes[i - 1].next = nodes[i]
            
    nodes[-1].next = None
        
    return nodes[0]

printList(sortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3))))))
printList(sortList(ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))))