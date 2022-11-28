import heapq

class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)

        target = [-x for x in target]
        heapq.heapify(target)
        
        while -target[0] > 1:
            largest = -target[0]
            rest = total - largest
        
            if rest == 1:
                return True
        
            a = largest % rest
        
            if a == 0 or a == largest:
                return False
            
            heapq.heapreplace(target, -a)
            total = total - largest + a
    
        return True

solution = Solution()
assert solution.isPossible([9, 3, 5]) == True
assert solution.isPossible([1, 1, 1, 2]) == False
assert solution.isPossible([8, 5]) == True