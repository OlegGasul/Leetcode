import bisect

class Solution:
    def shortestToChar(self, s: str, c: str):
        occurrencies = []
        
        for i in range(len(s)):
            if s[i] == c:
                occurrencies.append(i)
        
        result = [0] * len(s)
        
        if not occurrencies:
            return result
        
        for i in range(len(s)):
            if s[i] == c:
                continue
            
            index = bisect.bisect_left(occurrencies, i)
            if index == 0:
                result[i] = abs(i - occurrencies[index])
            elif index > len(occurrencies) - 1:
                result[i] = abs(i - occurrencies[-1])
            else:
                result[i] = min(abs(i - occurrencies[index]), abs(i - occurrencies[index - 1]))
        
        return result

solution = Solution()
print(solution.shortestToChar("loveleetcode", "e"))
print(solution.shortestToChar("aaab", "b"))