class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def createListNode(nums):
    head = ListNode(nums.pop())
    node = head

    while nums:
        node.next = ListNode(nums.pop())
        node = node.next

    return head

def printNodes(head):
    result = []
    
    while head:
        result.append(head.val)
        head = head.next

    print(result)


def deleteDuplicates(head):
    sentinel = ListNode(0, head)

    pred = sentinel
        
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
                
                pred.next = head.next 
        else:
            pred = pred.next 
                
        head = head.next
    
    return sentinel.next

printNodes(deleteDuplicates(createListNode([1, 2, 3, 3, 4, 4, 5])))