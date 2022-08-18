# https://leetcode.com/problems/2-keys-keyboard/

def minSteps(n: int) -> int:
    if n == 1:
        return 0

    count = 0

    for i in range(2, n + 1):
        if n % i == 0:
            count += i
            n //= i
            i -= 1
            
            if n == 1:
                return count

    return count
    

# print(minSteps(3))
# print(minSteps(8))
# print(minSteps(11))
# print(minSteps(25))
print(minSteps(741))

# A, CPP = AA, C, PP = 
# print(minSteps(99))

