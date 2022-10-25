def fizzBuzz(n: int):
    result = []
        
    i = 1
    while i <= n:
        word = ""
            
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0:
                word += "Fizz"
            if i % 5 == 0:
                word += "Buzz"
        else:
            word = str(i)
            
        result.append(word)
            
        i += 1
            
    return result

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))