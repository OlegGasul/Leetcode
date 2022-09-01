import functools

def sortByBits(arr):
    def countOfBits(n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count
        
    def compare(a, b):
        bits1 = countOfBits(a)
        bits2 = countOfBits(b)
            
        if bits1 == bits2:
            return a - b
        else:
            return bits1 - bits2
            
    
    arr = sorted(arr, key = functools.cmp_to_key(compare))
        
    return arr

print(sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))