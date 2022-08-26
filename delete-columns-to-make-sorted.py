def minDeletionSize(strs) -> int:
    result = 0
    length = len(strs[0])

    for i in range(length):
        prev = -1
        for word in strs:
            if ord(word[i]) < prev:
                result += 1
                break

            prev = ord(word[i])

    return result


print(minDeletionSize(["cba", "daf", "ghi"]))
print(minDeletionSize(["zyx", "wvu", "tsr"]))