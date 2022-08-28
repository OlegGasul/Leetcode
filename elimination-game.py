def lastRemaining(n: int) -> int:
    if n == 1:
        return 1

    if n == 2:
        return 2

    size = n // 2

    if n % 2 == 1:
        n -= 1

    incr = 2
    left = 2
    right = n
    
    direction = False # True - LR, False - RL

    while left < right:
        even = size % 2 == 0

        if direction:
            left += incr
            if not even:
                right -= incr
        else:
            right -= incr
            if not even:
                left += incr

        direction = not direction
            
        incr *= 2
        size //= 2

    return left

print(lastRemaining(9))
# print(lastRemaining(15))
