def threeConsecutiveOdds(arr) -> bool:
    counter = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            counter += 1
        else:
            counter = 0

        if counter == 3:
            return True

    return False

print(threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
print(threeConsecutiveOdds([2, 6, 4, 1]))