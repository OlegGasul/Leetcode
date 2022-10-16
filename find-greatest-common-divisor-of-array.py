import math

def findGCD(nums) -> int:
    minimum, maximum = float('inf'), -1
        
    for num in nums:
        minimum = min(minimum, num)
        maximum = max(maximum, num)
            
    return math.gcd(minimum, maximum)

print(findGCD([2, 5, 6, 9, 10]))
print(findGCD([7, 5, 6, 8, 3]))