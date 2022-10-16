# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

def average(salary) -> float:
    total = 0
    minimum = float('inf')
    maximum = float('-inf')
        
    for value in salary:
        minimum = min(minimum, value)
        maximum = max(maximum, value)
        total += value
            
    return (total - (minimum + maximum)) / (len(salary) - 2)

print(average([4000, 3000, 1000, 2000]))
print(average([1000, 2000, 3000]))
