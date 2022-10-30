class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def createNode(nums):
    head = ListNode(nums.pop(0))
    node = head

    while nums:
        node.next = ListNode(nums.pop(0))
        node = node.next

    return head

def spiralMatrix(m: int, n: int, head):
    mat = [[-1 for x in range(n)] for y in range(m)] 
        
    row = 0
    col = 0
        
    node = head
    while node and row < m and col < n:
            
        for j in range(col, n):
            if not node:
                break
            
            mat[row][j] = node.val
                    
            node = node.next
                    
        if not node:
            break
                
        for i in range(row + 1, m):
            if not node:
                break
                    
            mat[i][n - 1] = node.val
                
            node = node.next
                
        if not node:
            break
                
        for j in reversed(range(col, n - 1)):
            if not node:
                break
                    
            mat[m - 1][j] = node.val
                    
            node = node.next
                
        if not node:
            break
                
        for i in reversed(range(row + 1, m - 1)):
            if not node:
                break
                    
            mat[i][col] = node.val
                
            node = node.next
                
        if not node:
            break
                
        row += 1
        col += 1
        m -= 1
        n -= 1
            
    return mat

print(spiralMatrix(4, 5, createNode([515,942,528,483,20,159,868,999,474,320,734,956,12,124,224,252,909,732])))
print(spiralMatrix(3, 5, createNode([3,0,2,6,8,1,7,9,4,2,5,5,0])))