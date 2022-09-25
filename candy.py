import heapq

def candy(ratings) -> int:
    length = len(ratings)

    pq = []
    for i in range(length):
        pq.append((ratings[i], i))
    heapq.heapify(pq)

    candies = [0] * length
    result = 0

    while pq:
        rating, i = heapq.heappop(pq)
        candies[i] = max(candies[i - 1] + 1 if i - 1 >= 0 and ratings[i - 1] < rating else 1, candies[i + 1] + 1 if i + 1 < length and ratings[i + 1] < rating else 1)
        result += candies[i]

    return result


print(candy([1, 0, 2]))
print(candy([1, 2, 2]))