# If you observe carefully, it's really easy to bring negative signs adjacent to other, eg for [-1, 1, -1] we choose 0th and 1st index and get [1, -1, -1].
# Similar approach can be used for vertical cells.
# Two adjacent negative cells can be both made positive. In case of off odd number of negative or 0 cells in matrix, all cells except one will remain positive.
# The only negative will be cell with lowest absolute value. In case of even numbers of negative or 0 cells, all cells will remain positive.

# Just need to calculate total and leave 2 minimum cells if we have odd number of negative elements

def maxMatrixSum(matrix) -> int:
    total, count, mini = 0, 0, float('inf')

    for row in matrix:
        for cell in row:
            if cell <= 0:
                count += 1
            mini = min(mini, abs(cell))
            total += abs(cell)
    
    if count % 2 != 0:
        total -= 2 * mini
    
    return total


print(maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))