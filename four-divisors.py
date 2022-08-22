import math

def findDivisors(num):
    result = []
    i = 1

    while i <= math.sqrt(num):
        if num % i == 0:
            if num / i == i:
                result += [i]
            else:
                result += [i, num // i]

        if len(result) > 4:
            return []

        i += 1

    return result if len(result) == 4 else []


def sumFourDivisors(nums) -> int:
    divisors = {}
    result = []

    for i in range(len(nums)):
        if nums[i] in divisors:
            result += divisors[nums[i]]
            continue
        
        values = findDivisors(nums[i])
        result += values
        divisors[nums[i]] = values

    return sum(result)



print(sumFourDivisors([21, 4, 7]))
print(sumFourDivisors([21, 21]))
print(sumFourDivisors([1, 2, 3, 4, 5]))