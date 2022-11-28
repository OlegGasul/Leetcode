# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def findPivot():
            left = 1
            right = mountain_arr.length() - 2

            while left < right:
                middle = left + (right - left) // 2

                a = mountain_arr.get(middle - 1)
                value = mountain_arr.get(middle)
                b = mountain_arr.get(middle + 1)

                if value > a and value > b:
                    return middle
                
                if value > a and value < b:
                    left = middle + 1
                else:
                    right = middle - 1
            
            return left
        
        def searchTarget1(left, right):
            while left < right:
                middle = left + (right - left) // 2

                value = mountain_arr.get(middle)
                if value == target:
                    return middle
                
                if value < target:
                    left = middle + 1
                else:
                    right = middle - 1
            
            if left >= 0 and left < mountain_arr.length() and mountain_arr.get(left) == target:
                return left
            elif right >= 0 and right < mountain_arr.length() and mountain_arr.get(right) == target:
                return right
            else:
                return -1

        def searchTarget2(left, right):
            while left < right:
                middle = left + (right - left) // 2

                value = mountain_arr.get(middle)
                if value == target:
                    return middle
                
                if value < target:
                    right = middle - 1
                else:
                    left = middle + 1
            
            if left >= 0 and left < mountain_arr.length() and mountain_arr.get(left) == target:
                return left
            elif right >= 0 and right < mountain_arr.length() and mountain_arr.get(right) == target:
                return right
            else:
                return -1

        pivot = findPivot()
        result = searchTarget1(0, pivot)
        if result >= 0:
            return result
        
        return searchTarget2(pivot, mountain_arr.length() - 1)
        
