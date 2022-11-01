class Solution:
    def restoreString(self, s: str, indices) -> str:
        arr = [''] * len(s)
        
        for i in range(len(indices)):
            arr[indices[i]] = s[i]

        return ''.join(arr)

solution = Solution()
print(solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(solution.restoreString("abc", [0, 1, 2]))