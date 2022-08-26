def construct2DArray(original, m: int, n: int):
    length = len(original)
    if length / n != m :
        return []
    
    result = []
    i = 0

    while i < length:
        result.append(original[i : i + n])
        i += n

    return result



print(construct2DArray([1, 2, 3, 4], 2, 2))
print(construct2DArray([1, 2, 3], 1, 3))
print(construct2DArray([1, 2], 1, 1))