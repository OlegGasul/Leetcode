def reverseStr(s: str, k: int) -> str:
    length = len(s)
    position = 0
    result = ''

    while position < length:
        result += s[position : min(position + k, length)][::-1]
        position += k
        result += s[position : min(position + k, length)]
        position += k

    return result

print(reverseStr("abcdefg", 2))