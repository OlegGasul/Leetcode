from collections import Counter

def edgeScore(edges) -> int:
    length = len(edges)
    if length == 0:
        return 0
    
    counter = Counter()

    for i in range(len(edges)):
        counter[edges[i]] += i

    mostCommon = counter.most_common()
    maximum = mostCommon[0][1]
    values = [mostCommon[0][0]]

    for i in range(1, len(mostCommon)):
        if mostCommon[i][1] < maximum:
            break

        values.append(mostCommon[i][0])

    return min(values)
        


print(edgeScore([1, 0, 0, 0, 0, 7, 7, 5]))