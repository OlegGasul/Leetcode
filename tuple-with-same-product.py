from collections import Counter

def tupleSameProduct(nums) -> int:
    length = len(nums)
        
    counter = Counter()
        
    for i in range(length):
        for j in range(i + 1, length):
            counter[nums[i] * nums[j]] += 1

    result = 0
    for key, value in counter.most_common():
        if value < 2:
            break

        result += ((value * (value - 1)) // 2) * 8

    return result

print(tupleSameProduct([2, 3, 4, 6, 8, 12]))
print(tupleSameProduct([2, 3, 4, 6]))
print(tupleSameProduct([1, 2, 4, 5, 10]))