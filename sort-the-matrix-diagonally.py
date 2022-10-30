def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])
        
    for i in range(cols):
        values = []
            
        c = i
        r = 0
        while r < rows and c < cols:
            values.append(mat[r][c])
            r += 1
            c += 1
                
        values.sort()
            
        c = i
        r = 0
        while r < rows and c < cols:
            mat[r][c] = values.pop(0)
            r += 1
            c += 1
                
    for i in range(rows):
        values = []
            
        c = 0
        r = i
        while r < rows and c < cols:
            values.append(mat[r][c])
            r += 1
            c += 1
                
        values.sort()
            
        c = 0
        r = i
        while r < rows and c < cols:
            mat[r][c] = values.pop(0)
            r += 1
            c += 1
                
    return mat

print(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))