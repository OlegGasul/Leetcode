class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy, experience) -> int:
        result = 0
        
        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                result += energy[i] - initialEnergy + 1
                initialEnergy += energy[i] - initialEnergy + 1
                
            if initialExperience <= experience[i]:
                result += experience[i] - initialExperience + 1
                initialExperience += experience[i] - initialExperience + 1
                
            initialEnergy -= energy[i]
            initialExperience += experience[i]
                
        return result
                
solution = Solution()
print(solution.minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]))
print(solution.minNumberOfHours(2, 4, [1], [3]))