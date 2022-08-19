def reverseString(s):
    arr = list(s)
    
    length = len(arr)
    middle = length // 2
    
    for i in range(0, middle):
        arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]

    return ''.join(arr)

def reverseWords(s: str) -> str:
    strs = s.split(' ')

    for i in range(len(strs)):
        strs[i] = reverseString(strs[i])

    return ' '.join(strs)

print(reverseWords("Let's take LeetCode contest"))