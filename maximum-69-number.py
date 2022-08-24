def maximum69Number(num: int) -> int:
    numStr = str(num)
    length = len(numStr)
    
    for i in range(length):
        if numStr[i] == "6":
            return int(numStr[0:i] + "9" + numStr[i + 1 : length])

    return num

print(maximum69Number(9669))
print(maximum69Number(9999))
print(maximum69Number(9996))