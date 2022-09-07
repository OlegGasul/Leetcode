def sumEvenAfterQueries(nums, queries):
    evensTotal = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            evensTotal += nums[i]
                
    result = [0] * len(queries)
        
    for i in range(len(queries)):
        query = queries[i]
        if nums[query[1]] % 2 == 0:
            evensTotal -= nums[query[1]]
                
        nums[query[1]] += query[0]
        if nums[query[1]] % 2 == 0:
            evensTotal += nums[query[1]]
                
        result[i] = evensTotal
            
    return result

print(sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))