def createLinkedList(nums):
    root = ListNode(nums.pop(0))
    node = root

    for num in nums:
        node.next = ListNode(num)
        node = node.next

    return root

def printLinkedList(root):
    if not root:
        print([])
        return
    
    node = root
    result = []
    
    while node:
        result.append(node.val)
        node = node.next

    print(result)

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head:
            return None

        if not head.next:
            return head
        
        odd = head
        even = head.next
        firstEven = even

        isEven = False

        node = even.next

        while node:
            if isEven:
                even.next = node
                even = node
            else:
                odd.next = node
                odd = node
            
            node = node.next
            isEven = not isEven

        even.next = None
        odd.next = firstEven

        return head

solution = Solution()
printLinkedList(solution.oddEvenList(createLinkedList([1, 2, 3, 4, 5])))
printLinkedList(solution.oddEvenList(createLinkedList([2, 1, 3, 5, 6, 4, 7])))