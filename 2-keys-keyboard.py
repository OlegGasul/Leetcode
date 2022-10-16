# There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

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
    

print(minSteps(3))
print(minSteps(8))
print(minSteps(11))
print(minSteps(25))
print(minSteps(741))
print(minSteps(99))

