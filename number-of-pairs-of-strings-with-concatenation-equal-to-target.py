from collections import defaultdict

def numOfPairs(nums, target: str) -> int:
    parts = defaultdict(set)
        
    result = set()
        
    for i in range(len(nums)):
        if target.startswith(nums[i]):
            end = target[len(nums[i]) :]
            if end in parts:
                for index in parts[end]:
                    if i == index:
                        continue
                    result.add((i, index))
                        
        if target.endswith(nums[i]):
            start = target[:len(target) - len(nums[i])]
            if start in parts:
                for index in parts[start]:
                    if i == index:
                        continue
                    result.add((index, i))
                        
        parts[nums[i]].add(i)
            
    return len(result)

print(numOfPairs(["777", "7", "77", "77"], "7777"))
print(numOfPairs(["123", "4", "12", "34"], "1234"))