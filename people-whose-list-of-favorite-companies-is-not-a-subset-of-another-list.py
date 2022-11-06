from collections import defaultdict

class Solution:
    def peopleIndexes(self, favoriteCompanies):
        cache = defaultdict(set)

        for i in range(len(favoriteCompanies)):
            for company in favoriteCompanies[i]:
                cache[company].add(i)

        result = []

        for i in range(len(favoriteCompanies)):
            indecies = cache[favoriteCompanies[i][0]]
            
            for j in range(1, len(favoriteCompanies[i])):
                indecies = indecies.intersection(cache[favoriteCompanies[i][j]])

            if len(indecies) == 1:
                result.append(i)

        return result

solution = Solution()
print(solution.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))