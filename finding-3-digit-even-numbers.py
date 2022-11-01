from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        counter = Counter(digits)
        
        result = []
        
        for num in range(100, 1000):
            if num % 2 != 0:
                continue
                
            c = Counter()
            n = num
            while n:
                c[n % 10] += 1
                n //= 10
                
            equal = True
            for value, count in c.items():
                if counter[value] < count:
                    equal = False
                    break
                    
            if equal:
                result.append(num)
                
        return result

solution = Solution()
print(solution.findEvenNumbers([2, 1, 3, 0]))
print(solution.findEvenNumbers([2, 2, 8, 8, 2]))
print(solution.findEvenNumbers([3, 7, 5]))