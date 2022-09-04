def printList(node):
    result = []
            
    while node:
        result.append(node.val)
        node = node.next
    
    print(result)

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    def createList(node):
        result = []
            
        while node:
            result.append(node.val)
            node = node.next
                
        return result
        
    def createListNode(nums):
        root = ListNode(nums.pop())
        node = root

        while nums:
            node.next = ListNode(nums.pop())
            node = node.next
        
        return root
    
    l1 = createList(l1)
    l2 = createList(l2)
        
    carry = 0
    result = []

    while l1 or l2 or carry:
        a = l1.pop() if l1 else 0
        b = l2.pop() if l2 else 0
            
        value = a + b + carry
        result.append(value % 10)
            
        carry = 1 if value > 9 else 0

    return createListNode(result)

printList(addTwoNumbers(
    ListNode(7, ListNode(2, ListNode(4, ListNode(3)))),
    ListNode(5, ListNode(6, ListNode(4)))
))

printList(addTwoNumbers(
    ListNode(2, ListNode(4, ListNode(3))),
    ListNode(5, ListNode(6, ListNode(4)))
))

printList(addTwoNumbers(
    ListNode(0),
    ListNode(0)
))