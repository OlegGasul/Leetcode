import heapq

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

def mergeKLists(lists):
    if len(lists) == 0:
        return None
    
    values = []
    
    i = 0
    while len(lists) > 0:
        node = lists[-1]
        while node:
            heapq.heappush(values, node.val)
            node = node.next
        lists.pop()
    
    if len(values) == 0:
        return None

    root = ListNode(heapq.heappop(values))
    result = root

    while len(values) > 0:
        root.next = ListNode(heapq.heappop(values))
        root = root.next
    
    return result
        

printNodes(mergeKLists([
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(5, ListNode(7))),
    ListNode(10, ListNode(11))]))
