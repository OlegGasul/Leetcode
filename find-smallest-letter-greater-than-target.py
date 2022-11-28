class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
            
        return letters[0]

solution = Solution()
assert solution.nextGreatestLetter(["c", "f", "j"], "a") == "c"
assert solution.nextGreatestLetter(["c", "f", "j"], "c") == "f"