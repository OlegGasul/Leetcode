def generate(numRows: int):
    if numRows <= 0:
        return []
    
    result = [[1]]
    
    if numRows == 1:
        return result

    prev = result[0]
    
    for i in range(1, numRows):
        arr = [1]

        for j in range(1, len(prev)):
            arr.append(prev[j - 1] + prev[j])

        arr.append(1)

        result.append(arr)

        prev = arr

    return result
        
    

print(generate(5))