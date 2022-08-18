def validSquare(p1, p2, p3, p4) -> bool:
    # pick p1: calculate the vector from p1 to p2, p3, and p4
    v = [(x - p1[0], y - p1[1]) for x, y in [p2, p3, p4]]
    print(v)
        
    # calculate the distance p2, p3, p4 are from p1 
    (d1, (x1, y1)), (d2, (x2, y2)), (d3, (x3, y3)) = sorted([(x ** 2 + y ** 2, (x, y)) for x, y in v])

    print(x1, y1, x2, y2, x3, y3)
    print(d1, d2, d3)
        
    # for p1,p2,p3,p4 to form a square
    # 1. the shorted vector must have none zero length
    # 2. then out of the three remaining vectors, 2 of them must be the same 
    # 3. the sum of the two shorter vectors must equal the longer vector 
    # 4. using pythagoras theorem, the square of the lengths of ther two shorter 
    #    vectors must sum up to that of the longer one.
    return d1 != 0 and d1 == d2 and x1 + x2 == x3 and y1 + y2 == y3 and d1 + d2 == d3


# print(validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
print(validSquare([1, 0], [-1, 0], [0, 1], [0, -1]))