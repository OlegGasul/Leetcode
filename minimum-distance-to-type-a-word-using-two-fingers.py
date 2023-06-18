import heapq

lettersMap = {
    'A': [0, 0],
    'B': [0, 1],
    'C': [0, 2],
    'D': [0, 3],
    'E': [0, 4],
    'F': [0, 5],
    'G': [1, 0],
    'H': [1, 1],
    'I': [1, 2],
    'J': [1, 3],
    'K': [1, 4],
    'L': [1, 5],
    'M': [2, 0],
    'N': [2, 1],
    'O': [2, 2],
    'P': [2, 3],
    'Q': [2, 4],
    'R': [2, 5],
    'S': [3, 0],
    'T': [3, 1],
    'U': [3, 2],
    'V': [3, 3],
    'W': [3, 4],
    'X': [3, 5],
    'Y': [4, 0],
    'Z': [4, 1]
}

class Solution:
    def minimumDistance(self, word: str) -> int:
        length = len(word)
        newWord = [word[0]]
        
        for i in range(1, length):
            if word[i] == word[i - 1]:
                continue
            newWord.append(word[i])
        
        word = newWord
        length = len(word)
        if length <= 2:
            return 0

        def getKey(letters, position):
            ch1, ch2 = letters
            key = [ch1, ch2]
            key.sort()
            return (key[0], key[1], position)

        def getDistance(ch1, ch2):
            a, b = lettersMap[ch1]
            c, d = lettersMap[ch2]
            return abs(a - c) + abs(b - d)

        current = [word[0], word[1]]
        
        key = getKey(current, 1)
        distances = {key: 0}
        
        pq = []
        dist = 0
        heapq.heappush(pq, [dist, getKey(current, 1)])
        
        for i in range(2, length):
            dist += getDistance(current[0], word[i - 1])
            current = [word[i - 1], word[i]]
            key = getKey(current, i)
            distances[key] = dist
            heapq.heappush(pq, [dist, key])

        result = float('inf')
        
        while pq:
            dist, key = heapq.heappop(pq)
            ch1, ch2, pos = key

            if pos == length - 1:
                result = min(result, dist)
                continue

            nextPos = pos + 1
            nextCh = word[nextPos]
            
            d1 = getDistance(ch1, nextCh)
            key1 = getKey([ch2, nextCh], nextPos)
            if not key1 in distances or distances[key1] > dist + d1:
                distances[key1] = dist + d1
                heapq.heappush(pq, [dist + d1, key1])
            
            d2 = getDistance(ch2, nextCh)
            key2 = getKey([ch1, nextCh], nextPos)
            if not key2 in distances or distances[key2] > dist + d2:
                distances[key2] = dist + d2
                heapq.heappush(pq, [dist + d2, key2])

        return result


solution = Solution()
assert solution.minimumDistance("CAKE") == 3
assert solution.minimumDistance("HAPPY") == 6