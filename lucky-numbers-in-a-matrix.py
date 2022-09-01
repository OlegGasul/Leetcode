def luckyNumbers(matrix):
    rowsLength = len(matrix)
    colsLength = len(matrix[0])
        
    rows = [-1] * rowsLength
    cols = [-1] * colsLength

    def findMinRowIndex(row):
        if rows[row] > 0:
            return rows[row]
        
        minimum = float('inf')
        minimumIndex = -1
            
        for i in range(colsLength):
            if matrix[row][i] < minimum:
                minimum = matrix[row][i]
                minimumIndex = i
            
        rows[row] = minimumIndex
        return minimumIndex
        
    def findMaxColIndex(col):
        if cols[col] > 0:
            return cols[col]
        
        maximum = float('-inf')
        maximumIndex = -1
            
        for i in range(rowsLength):
            if matrix[i][col] > maximum:
                maximum = matrix[i][col]
                maximumIndex = i
        
        cols[col] = maximumIndex
        return maximumIndex
        
    for i in range(rowsLength):
        col = findMinRowIndex(i)
        index = findMaxColIndex(col)

        if index == i:
            return [matrix[i][col]]

    return []


print(luckyNumbers([
    [1, 10, 4, 2],
    [9, 3, 8, 7],
    [15, 16, 17, 12]]))

print(luckyNumbers([
    [9, 3, 8, 7],
    [1, 10, 4, 2],
    [15, 16, 17, 12]]))

print(luckyNumbers([
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17]]))

print(luckyNumbers([
    [7, 8],
    [1, 2]]))

print(luckyNumbers([
    [3, 6],
    [7, 1],
    [5, 2],
    [4, 8]]))