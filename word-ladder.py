from collections import defaultdict
import heapq

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if beginWord == endWord:
            return 0
        
        words = defaultdict(set)
        masks = defaultdict(set)
        
        def putWordToMappings(word):
            for i in range(len(word)):
                mask = word[ : i] + "*" + word[i + 1 : ]
                masks[word].add(mask)
                words[mask].add(word)

        for word in wordList:
            putWordToMappings(word)
        
        if not endWord in masks:
            return 0

        putWordToMappings(beginWord)
        putWordToMappings(endWord)

        graph = defaultdict(set)
        for word in masks:
            edges = set()
            for m in masks[word]:
                graph[word].update(words[m])
            if word in graph[word]:
                graph[word].discard(word)


        distances = {}
        distances[beginWord] = 0

        visited = set()
        
        pq = []
        pq.append((0, beginWord))
        heapq.heapify(pq)

        while pq:
            minValue, word = heapq.heappop(pq)
            visited.add(word)

            for edge in graph[word]:
                if edge in visited:
                    continue

                newDistance = distances[word] + 1
                if  not edge in distances or newDistance < distances[edge]:
                    distances[edge] = newDistance
                    heapq.heappush(pq, (newDistance, edge))
                    heapq.heapify(pq)
        
        return distances[endWord] + 1 if endWord in distances else 0

solution = Solution()
assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
assert solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0