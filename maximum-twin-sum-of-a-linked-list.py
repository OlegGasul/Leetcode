class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def pairSum(head) -> int:
    node = head
        
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
            
    length = len(nums)
    result = float('-inf')
        
    for i in range(len(nums)):
        result = max(result, nums[i] + nums[length - i - 1])
            
    return result

print(pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1)))))))