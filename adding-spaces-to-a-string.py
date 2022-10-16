# You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

# For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
# Return the modified string after the spaces have been added.

def addSpaces(s: str, spaces) -> str:
    if s == None or s == "":
        return ""

    if spaces == None or len(spaces) == 0:
        return s
    
    spaces = sorted(spaces)
        
    length = len(s)
    prev = 0
    arr = []
    
    for x in spaces:
        if x > length:
            break
            
        arr.append(s[prev : x])
        prev = x

    arr.append(s[prev : length])

    return ' '.join(arr)


print(addSpaces("LeetcodeHelpsMeLearn", [7, 8, 13, 15, 100]))
print(addSpaces("LeetcodeHelpsMeLearn", [100]))
print(addSpaces("LeetcodeHelpsMeLearn", []))
print(addSpaces(None, [7, 8, 13, 15, 100]))
print(addSpaces(None, [7, 8, 13, 15, 100]))
