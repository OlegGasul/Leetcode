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

def middleNode(head):
    if not head:
        return None
        
    node = head
        
    nums = []
    while node:
        nums.append(node)
        node = node.next
            
    return nums[len(nums) // 2]

printNodes(middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))