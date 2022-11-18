from collections import Counter

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        reminders = Counter()

        for n in arr:
            if k - n % k in reminders:
                key = k - n % k
                reminders[key] -= 1
                if reminders[key] == 0:
                    del reminders[key]
            else:
                reminders[k if n % k == 0 else n % k] += 1

        return not any(reminders.values())

solution = Solution()
print(solution.canArrange([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5))
print(solution.canArrange([1, 2, 3, 4, 5, 6], 5))
print(solution.canArrange([1, 2, 3, 4, 5, 6], 10))