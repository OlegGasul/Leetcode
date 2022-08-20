# https://stackoverflow.com/questions/52395099/meaning-of-list-1-in-python#:~:text=%5B%2D1%5D%20means%20the%20last,element%20in%20the%20original%20collection.
# So, if you wanted the last element in array, you would call array[-1].

def removeKdigits(num: str, k: int) -> str:
    stack = []
    for n in num:
        
        while k and stack and stack[-1] > n:
            stack.pop()
            k -= 1
        
        stack.append(n)

    for _ in range(k): stack.pop()
    
    return ''.join(stack).lstrip('0') or '0'



print(removeKdigits("1791924", 3))
print(removeKdigits("123456", 3))