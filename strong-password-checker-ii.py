def strongPasswordCheckerII(password: str) -> bool:
    length = len(password)
    if length < 8:
        return False

    specials = set("!@#$%^&*()-+")

    lower = False
    upper = False
    digit = False
    special = False

    for i in range(length):
        char = password[i]

        if i > 0 and char == password[i - 1]:
            return False
        if char.islower():
            lower = True
        if char.isupper():
            upper = True
        if char.isdigit():
            digit = True
        if char in specials:
            special = True
        
    return lower and upper and digit and special
        

print(strongPasswordCheckerII("IloveLe3tcode!"))
print(strongPasswordCheckerII("Me+You--IsMyDream"))
print(strongPasswordCheckerII("1aB!"))
print(strongPasswordCheckerII("IloveLe3tcode!aa"))