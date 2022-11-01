class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        
        for i in range(len(command)):
            if command[i].isalpha():
                result += command[i]
            elif command[i] == ")" and command[i - 1] == "(":
                result += "o"
                
        return result

solution = Solution()
print(solution.interpret("G()(al)"))
print(solution.interpret("G()()()()(al)"))
print(solution.interpret("(al)G(al)()()G"))