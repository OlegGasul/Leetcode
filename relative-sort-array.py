from functools import cmp_to_key

def relativeSortArray(arr1, arr2):
    length = len(arr2)

    indexes = {}
    for i, x in enumerate(arr2):
        indexes[x] = i

    def compare(a, b):
        val1 = indexes[a] if a in indexes else length + a
        val2 = indexes[b] if b in indexes else length + b
        return val1 - val2

    return sorted(arr1, key = cmp_to_key(compare))

print(relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))