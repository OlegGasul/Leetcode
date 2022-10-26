def distributeCandies(candies: int, num_people: int):
    result = [0] * num_people
        
    incr = 0
        
    while candies:
            
        for i in range(num_people):
            incr += 1
                
            if incr > candies:
                result[i] += candies
                return result
            else:
                result[i] += incr
                candies -= incr
                    
    return result

print(distributeCandies(7, 4))
print(distributeCandies(10, 3))