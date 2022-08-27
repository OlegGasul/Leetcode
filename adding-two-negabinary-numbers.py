from time import sleep

def printResult(arr1, arr2):
    a = int(''.join([str(x) for x in arr1]), 2)
    b = int(''.join([str(x) for x in arr2]), 2)
    print(str(a) + ' + ' + str(b) + ' = ' + (str(a + b)))

    print(addNegabinary(arr1, arr2))


def addNegabinary(arr1, arr2):
    result = []
    curry = 0

    while arr1 or arr2 or curry == 1:
        bit1 = arr1.pop() if arr1 else 0
        bit2 = arr2.pop() if arr2 else 0
        
        value = bit1 ^ bit2

        if curry == 1:
            value ^= curry
            if value == 0:
                curry = 1
        
        result.insert(0, value)

    return result


# printResult([0, 1, 0], [1, 0, 1])
# printResult([1, 0, 1, 0], [1, 1, 1])
printResult([1, 1, 1, 1, 1], [1, 0, 1])