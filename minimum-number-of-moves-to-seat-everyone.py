def minMovesToSeat(seats, students) -> int:
    seats.sort()
    students.sort()
        
    result = 0
        
    for i in range(len(seats)):
        result += abs(seats[i] - students[i])
            
    return result

print(minMovesToSeat([3, 1, 5], [2, 7, 4]))
print(minMovesToSeat([4, 1, 5, 9], [1, 3, 2, 6]))