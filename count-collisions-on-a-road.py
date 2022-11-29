class Solution:
    def countCollisions(self, directions: str) -> int:
        i = 0
        while i < len(directions):
            if directions[i] != "L":
                break
            
            i += 1
        
        j = len(directions) - 1
        while j >= i:
            if directions[j] != "R":
                break
            
            j -= 1

        result = 0
        for k in range(i, j + 1):
            if directions[k] != "S":
                result += 1
        
        return result
        
solution = Solution()
solution.countCollisions("RLRSLL")
solution.countCollisions("LLRR")