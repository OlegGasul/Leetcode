import functools

def maximumBeauty(items, queries):
    def compare(a, b):
        if a[0] == b[0]:
            return b[1] - a[1]
        else:
            return a[0] - b[0]

    items = sorted(items, key = functools.cmp_to_key(compare))
    
    i = 1
    while i < len(items):
        if items[i][0] == items[i - 1][0] and items[i][1] < items[i - 1][1]:
            items.pop(i)
        else:
            i += 1

    dp = [0] * len(items)
    dp[0] = items[0][1]
    for i in range(1, len(items)):
        dp[i] = max(dp[i - 1], items[i][1])

    def findMostBeautiful(price):
        if price < items[0][0]:
            return 0
        
        left = 0
        right = len(items) - 1

        while left < right - 1:
            middle = left + (right - left) // 2
            
            if price < items[middle][0]:
                right = middle - 1
            else:
                left = middle
            
        return dp[right] if price >= items[right][0] else dp[left]
    
    for i in range(len(queries)):
        queries[i] = findMostBeautiful(queries[i])

    return queries
        

print(maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
print(maximumBeauty([[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [4]))
print(maximumBeauty([[1, 2], [1, 2], [1, 3], [1, 4]], [1]))
print(maximumBeauty([[10, 1000]], [5]))

print(maximumBeauty(
    [[193, 732], [781, 962], [864, 954], [749, 627], [136, 746], [478, 548], [640, 908], [210, 799], [567, 715], [914, 388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]],
    [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]))
