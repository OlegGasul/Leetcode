def rearrangeBarcodes(barcodes):
    length = len(barcodes)
    if length <= 1:
        return barcodes
    
    barcodes = sorted(barcodes)
    # print(barcodes)
    result = []
    
    middle = length // 2
    for i in range(0, middle):
        if barcodes[i] == barcodes[length - i - 1]:
            result.insert(0, barcodes[i])
        else:
            result.append(barcodes[i])
        result.append(barcodes[length - i - 1])

    if length % 2 == 1:
        result.append(barcodes[middle])

    return result

# print(rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
# print(rearrangeBarcodes([1, 1, 2]))
# print(rearrangeBarcodes([2, 2, 1, 3]))
print(rearrangeBarcodes([2, 2, 2, 1, 5]))
