def selfDividingNumbers(left: int, right: int):
    result = []
    if left <= 10:
        result += list(range(max(1, left), 10))
    
    for num in range(max(left, 10), right + 1):
        nums = list(str(num))
        counter = 0
            
        for digit in nums:
            digit = int(digit)
            if digit == 0 or num % digit != 0:
                break
            counter += 1
                
        if counter == len(nums):
            result.append(num)
        
    return result

print(selfDividingNumbers(1, 22))