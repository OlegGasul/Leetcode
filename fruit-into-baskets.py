def totalFruit(fruits) -> int:
    length = len(fruits)
    maxTrees = 0
    
    left = 0
    right = 0
    
    trees = { }
    trees[fruits[0]] = 1
    
    while left < length and right < length:
        # print()
        # print('left = ' + str(left))
        # print('right = ' + str(right))
        # print(trees)

        keys = len(trees.keys())
        if keys <= 2:
            maxTrees = max(right - left + 1, maxTrees)
            # print('maxTrees = ' + str(maxTrees))

            right += 1
            if right < length:
                if not fruits[right] in trees:
                    trees[fruits[right]] = 0
                trees[fruits[right]] += 1
        else:
            if left < right:
                trees[fruits[left]] -= 1
                if trees[fruits[left]] == 0:
                    trees.pop(fruits[left], None)
                
                left += 1
            else:
                right += 1
                if right < length:
                    if not fruits[right] in trees:
                        trees[fruits[right]] = 0
                    trees[fruits[right]] += 1

                        
    return maxTrees



print(totalFruit([1, 2, 1]))
print(totalFruit([0, 1, 2, 2]))
print(totalFruit([1, 2, 3, 2, 2]))

print(totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))
