def arrayRankTransform(nums):
    ranks = {}
    i = 0
    for num in sorted(nums):
	    if not num in ranks:
		    i += 1
		    ranks[num] = i
    
    for i in range(len(nums)):
	    nums[i] = ranks[nums[i]]
    
    return nums

print(arrayRankTransform([40, 10, 20, 30]))
print(arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))