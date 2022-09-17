class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def getDecimalValue(head) -> int:
    node = head
    result = 0
    
    while node:
        result |= node.val

        node = node.next
        if node:
            result <<= 1
            
    return result

print(getDecimalValue(ListNode(1, ListNode(0, ListNode(1, ListNode(0))))))
print(getDecimalValue(ListNode(1, ListNode(0, ListNode(1, ListNode(0, ListNode(1)))))))
print(getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))))
print(getDecimalValue(ListNode(0)))