from functools import cmp_to_key

def customSortString(order: str, s: str) -> str:
    orderList = list(order)

    indexes = {}
    for i, x in enumerate(orderList):
        indexes[x] = i

    length = len(orderList)

    def compare(a, b):
        index1 = indexes[a] if a in indexes else length
        index2 = indexes[b] if b in indexes else length
        return index1 - index2

    return ''.join(sorted(list(s), key = cmp_to_key(compare)))


print(customSortString("cba", "abcd"))
print(customSortString("cbafg", "abcd"))