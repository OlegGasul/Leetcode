def mergeSimilarItems(items1, items2):
    if len(items1) == 0 or len(items2) == 0:
        return items1 + items2
    
    items = sorted(items1 + items2, key = lambda x: x[0])

    i = 1
    while i < len(items):
        if items[i - 1][0] == items[i][0]:
            items[i - 1][1] = items[i - 1][1] + items[i][1]
            items.pop(i)
        else:
            i += 1

    return items


print(mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))