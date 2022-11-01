class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        
        for ch in s:
            if not ch.isdigit():
                continue
                
            nums.add(int(ch))
            
        if len(nums) < 2:
            return -1
        
        return sorted(list(nums))[-2]

solution = Solution()
print(solution.secondHighest("dfa12321afd"))
print(solution.secondHighest("abc1111"))