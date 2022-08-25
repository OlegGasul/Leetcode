def platesBetweenCandles(s: str, queries):
    length = len(s)
    
    plates = [0] * length
    candlesFromLeft = [0] * length
    candlesFromRight = [0] * length
    
    candle = -1

    for i in range(length):
        plates[i] = plates[i - 1] + (1 if s[i] == '*' else 0)
        
        if s[i] == '|':
            candle = i
        candlesFromLeft[i] = candle

    candle = -1

    for i in reversed(range(length)):
        if s[i] == '|':
            candle = i
        candlesFromRight[i] = candle

    result = [0] * len(queries)

    for i in range(len(queries)):
        query = queries[i]
        
        left = max(query[0], candlesFromRight[query[0]])
        right = min(query[1], candlesFromLeft[query[1]])
        if left < right:
            result[i] = plates[right] - plates[left]

        # print('candles[query[0]] = ' + str(candlesFromRight[query[0]]))
        # print('candles[query[1]] = ' + str(candlesFromLeft[query[1]]))
        

    # print(plates)
    # print(candlesFromLeft)
    # print(candlesFromRight)

    return result

print(platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]))
print(platesBetweenCandles("**|**|***|*", [[1, 6], [0, 1], [6, 8], [2, 9]]))