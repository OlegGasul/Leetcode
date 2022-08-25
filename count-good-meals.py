from collections import defaultdict

def countPairs(deliciousness) -> int:
    mod = 10 ** 9 + 7

    maximum = 1 << 22
    count = defaultdict(int)
    result = 0
    
    for item in deliciousness:
        i = 1
        while i < maximum:
            value = i - item
            if value in count:
                result += count[value]
                if result > mod:
                    result -= mod
            i <<= 1
        count[item] += 1
            
    return result

print(countPairs([1, 3, 5, 7, 9]))
print(countPairs([1, 1, 1, 3, 3, 3, 7]))