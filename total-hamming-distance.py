def totalHammingDistance(nums) -> int:
    if len(nums) <= 1:
        return 0

    cache = {}

    def hammingDistance(x: int, y: int) -> int:
        if x == y:
            return 0

        nonlocal cache

        counter = 0
        while x > 0 or y > 0:
            key = (x, y)
            if key in cache:
                return counter + cache[key]
            
            value = (x & 1) ^ (y & 1)
            cache[key] = value
            
            counter += value
            x = x >> 1 if x > 0 else 0
            y = y >> 1 if y > 0 else 0

        return counter

    total = 0

    nums = sorted(list(set(nums)))
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            key = (nums[i], nums[j])
            if key in cache:
                value = cache[key]
            else:
                value = hammingDistance(nums[i], nums[j])
                cache[key] = value
            
            total += value

    return total

print(totalHammingDistance([4, 14, 2]))