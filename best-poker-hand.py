from collections import Counter

class Solution:
    def bestHand(self, ranks, suits) -> str:
        suitsCounter = Counter(suits)
        maxSuits = suitsCounter.most_common()[0][1]
        if maxSuits == 5:
            return "Flush"
        
        ranksCounter = Counter(ranks)
        maxRanks = ranksCounter.most_common()[0][1]
        if maxRanks >= 3:
            return "Three of a Kind"
        if maxRanks == 2:
            return "Pair"
        
        return "High Card"
        
solution = Solution()
print(solution.bestHand([13, 2, 3, 1, 9], ["a", "a", "a", "a", "a"]))
print(solution.bestHand([4, 4, 2, 4, 4], ["d", "a", "a", "b", "c"]))
print(solution.bestHand([10, 10, 2, 12, 9], ["a", "b", "c", "a", "d"]))